# Projeto de Automação Assistente de IA Bancário

Este projeto implementa uma suite de testes automatizados para validar um Assistente de IA Bancário usando Gherkin (BDD), Playwright, Langfuse e uma rúbrica matemática de fidelidade (faithfulness).

## 📋 Estrutura do Projeto

```
.
├── manual_banco.txt              # Base de conhecimento RAG para a IA
├── requirements.txt              # Dependências Python
├── features/
│   ├── ia_bancaria.feature       # Cenários Gherkin
│   ├── steps.py                  # Implementação dos steps com Playwright e Langfuse
│   └── conftest.py               # Configuração do Behave
└── README_QA_IA_BANCARIA.md      # Este arquivo
```

## 🎯 Objetivo

Validar se o Assistente de IA Bancário responde corretamente sobre saldos e informações bancárias usando RAG (Retrieval-Augmented Generation), garantindo que as respostas tenham fidelidade maior que 0.80 através de uma rúbrica matemática.

## 🚀 Tecnologias Utilizadas

- **Gherkin/Behave**: Framework BDD para escrever cenários em linguagem natural
- **Playwright**: Automação web para interação com a interface
- **Langfuse**: SDK para tracing e monitoramento de LLM
- **Python 3.8+**: Linguagem de programação


```

## 📊 Rúbrica de Fidelidade (Faithfulness)

A rúbrica matemática calcula a fidelidade da resposta da IA baseada em 4 critérios:

1. **Precisão do valor numérico (40%)**: Verifica se o valor monetário está correto
2. **Presença de contexto relevante (30%)**: Verifica palavras-chave relevantes
3. **Formatação correta (20%)**: Verifica se a resposta está formatada como moeda
4. **Ausência de alucinações (10%)**: Verifica se a resposta não contradiz o contexto

**Fórmula**:
```
Fidelidade = (Precisão × 0.4) + (Contexto × 0.3) + (Formatação × 0.2) + (Sem Alucinações × 0.1)
```

**Critério de aprovação**: Score > 0.80

## 📝 Cenários de Teste

O projeto inclui 8 cenários de teste:

1. ✅ Consulta de saldo da conta corrente
2. ✅ Consulta de saldo da conta poupança
3. ✅ Consulta de saldo disponível com limite
4. ✅ Consulta de saldo total de todas as contas
5. ❌ Consulta de saldo com informação incorreta (teste de falha)
6. ✅ Consulta de limite do cartão de crédito
7. ✅ Consulta de fatura atual do cartão
8. ✅ Consulta de informações de empréstimo

## 🔍 Tracing com Langfuse

Todos os testes registram traces no Langfuse com:
- Pergunta feita à IA
- Resposta da IA
- Score de fidelidade
- Nome do cenário
- Tipo de teste


## 📈 Relatórios

### Gerar relatório HTML

```bash
pip install behave-html-formatter
behave -f behave_html_formatter:PrettyHTMLFormatter -o reports/report.html
```

### Gerar relatório JSON

```bash
behave -f json -o reports/report.json
```

## 🔐 Segurança

- Credenciais e chaves privadas de API são consumidas estritamente via variáveis de ambiente.
- O arquivo de configuração local (`.env`) encontra-se devidamente mapeado no `.gitignore`.


## 🎉 Exemplo de Execução

```bash
$ behave
======================================================================
🚀 INICIANDO SUITE DE TESTES - ASSISTENTE IA BANCÁRIO
======================================================================
✅ Manual do banco encontrado: /path/to/manual_banco.txt
✅ Langfuse configurado
✅ Playwright pronto para uso

📋 Cenário: Consulta de saldo da conta corrente
----------------------------------------------------------------------
📝 Pergunta: Qual é o saldo da minha conta corrente?
🤖 Resposta da IA: O saldo da sua conta corrente é de R$ 5.450,00...
✅ Valor correto verificado: R$ 5450.00

📊 Score de Fidelidade: 0.95
✅ Fidelidade aprovada: 0.95 > 0.80
✅ Trace registrado no Langfuse para o cenário: Consulta de saldo da conta corrente
----------------------------------------------------------------------
✅ CENÁRIO APROVADO: Consulta de saldo da conta corrente
   Score de Fidelidade: 0.95

======================================================================
🏁 SUITE DE TESTES FINALIZADA
======================================================================
```


