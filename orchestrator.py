import os
import re
from langfuse import Langfuse
from dotenv import load_dotenv

load_dotenv()

class AIAssistentOrchestrator:
    def __init__(self):
        # Inicializa o Langfuse usando as variáveis de ambiente
        self.langfuse = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY", "mock_public_key"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY", "mock_secret_key"),
            host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        )
        self.kb_path = "manual_banco.txt"

    def _retrieve_context(self, query: str) -> str:
        """
        Mecânica simplificada de RAG (Retrieval): Busca as seções relevantes 
        no manual_banco.txt com base em palavras-chave da query.
        """
        if not os.path.exists(self.kb_path):
            return "Contexto indisponível: manual_banco.txt não encontrado."
            
        with open(self.kb_path, "r", encoding="utf-8") as f:
            content = f.read()

        # RAG Engine de Portfólio: Segmenta por blocos de tópicos do manual
        sections = content.split("========================================")
        relevant_chunks = []
        
        # Palavras-chave para busca heurística
        keywords = ["SALDO", "POUPANÇA", "LIMITE", "CARTÃO", "FATURA", "EMPRÉSTIMO", "CORRENTE"]
        found_words = [w for w in keywords if w in query.upper()]

        for section in sections:
            if any(word in section.upper() for word in found_words):
                relevant_chunks.append(section.strip())

        return "\n\n".join(relevant_chunks) if relevant_chunks else content[:1000]

    def calculate_faithfulness(self, response: str, context: str, expected_value: str) -> float:
        """
        Implementação determinística da Rúbrica Matemática de Fidelidade:
        Fidelidade = (Precisão × 0.4) + (Contexto × 0.3) + (Formatação × 0.2) + (Sem Alucinações × 0.1)
        """
        # 1. Precisão do valor numérico (40%)
        # Remove caracteres não numéricos para comparar os valores crutos
        expected_digits = "".join(filter(str.isdigit, expected_value))
        response_digits = "".join(filter(str.isdigit, response))
        precision = 1.0 if expected_digits in response_digits and expected_digits != "" else 0.0

        # 2. Presença de contexto relevante (30%)
        # Verifica se termos chave do contexto aparecem na resposta da IA
        context_keywords = ["conta", "saldo", "joão", "silva", "cartão", "empréstimo"]
        matched_keywords = [w for w in context_keywords if w in response.lower()]
        context_score = len(matched_keywords) / len(context_keywords)

        # 3. Formatação correta como moeda R$ (20%)
        formatting = 1.0 if "R$" in response else 0.0

        # 4. Ausência de alucinações (10%)
        # Critério: A IA não pode inventar bancos ou valores financeiros que não estão no contexto
        hallucination_detected = False
        all_numbers_in_response = re.findall(r"\d+(?:\.\d+)?", response.replace(".", "").replace(",", "."))
        for num in all_numbers_in_response:
            if float(num) > 0 and "".join(filter(str.isdigit, str(num))) not in "".join(filter(str.isdigit, context)):
                hallucination_detected = True
                break
        no_hallucination = 0.0 if hallucination_detected else 1.0

        # Aplicação da fórmula ponderada
        faithfulness = (precision * 0.4) + (context_score * 0.3) + (formatting * 0.2) + (no_hallucination * 0.1)
        return round(faithfulness, 2)

    def execute_ai_query(self, scenario_name: str, query: str, expected_value: str, mock_response: str = None) -> dict:
        """
        Orquestra a chamada RAG, gera/simula a resposta, calcula as rúbricas 
        e registra o trace completo no dashboard do Langfuse.
        """
        # 1. Recupera o Contexto (RAG Retrieval)
        context = self._retrieve_context(query)

        # 2. Geração da Resposta (Modo Produção Real vs Simulação de Portfólio)
        # Para usar produção real, bastaria plugar a chamada de API da LLM aqui usando o context
        ai_response = mock_response if mock_response else f"O saldo verificado no sistema para a sua solicitação é de {expected_value}."

        # 3. Avaliação de Qualidade (Métricas de QA)
        score = self.calculate_faithfulness(ai_response, context, expected_value)

        # 4. Observabilidade - Registro de Trace no Langfuse
        trace = self.langfuse.trace(
            name=scenario_name,
            user_id="luciana_orli_qa_sr",
            metadata={"interface": "playwright_web", "type": "rag_evaluation"}
        )
        
        # Span da busca RAG
        trace.span(
            name="rag_retrieval",
            input={"query": query},
            output={"context_length": len(context)}
        )

        # Generation da LLM com a pontuação acoplada
        generation = trace.generation(
            name="llm_generation",
            input=f"Contexto: {context}\n\nPergunta: {query}",
            output=ai_response
        )
        
        # Envia o Score da Rúbrica diretamente para o painel do Langfuse
        generation.score(
            name="faithfulness",
            value=score,
            comment="Cálculo matemático automatizado via suíte de testes BDD."
        )

        return {
            "query": query,
            "response": ai_response,
            "score": score,
            "passed": score > 0.80
        }
