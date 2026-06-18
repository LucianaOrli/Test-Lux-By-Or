# 🤖 Projeto LuxBYOr: Automação e Observabilidade para Assistente de IA Bancário

# Visão Geral

Este projeto implementa uma estratégia de automação para validação de um Assistente de IA Bancário baseado em RAG (Retrieval-Augmented Generation).

A solução foi desenvolvida utilizando BDD (Behavior-Driven Development) com Gherkin, Python e Behave, incorporando mecanismos de avaliação automática da qualidade das respostas e observabilidade através do Langfuse.

Não é apenas verificar se uma resposta foi retornada, mas avaliar se ela é consistente, aderente ao contexto consultado e suficientemente confiável para cenários de negócio.

# 🎯 Objetivo
 A suíte de testes foi construída para validar:
 Precisão das informações apresentadas pela IA.
 Fidelidade das respostas baseada em rúbrica matemática
 Observabilidade através de traces no Langfuse
 Comportamento em cenários positivos e negativos /  Cobertura de cenários de sucesso e falha.
 Consistência dos resultados gerados.
 Rastreabilidade completa das execuções através do Langfuse.


## 🏗️ Estrutura do Projeto

```
.
├── .github/                 # Configurações do GitHub (CI/CD, Issues)
├── docs/                    # Documentação e evidências
│   ├── evidencias/          # Evidências de testes (screenshots, logs)
│   └── relatorios/          # Relatórios de execução
├── features/                # Arquivos Gherkin (.feature)
│   ├── ia_bancaria.feature  # Cenários de teste em português
│   └── steps/               # Implementação dos steps
│       ├── steps.py         # Lógica dos steps em Python
│       └── __init__.py
├── reports/                 # Relatórios gerados pelo Behave
├── .behave/                 # Cache do Behave
├── .env.example             # Exemplo de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── behave.ini               # Configuração do Behave
├── conftest.py              # Configuração de hooks do Behave
├── manual_banco.txt         # Base de conhecimento RAG
├── requirements.txt         # Dependências Python
└── README.md                # Este arquivo

 Tecnologias Utilizadas

 **Python 3.8+**: Linguagem principal pip (gerenciador de pacotes Python)
 **Behave**: Framework BDD para Python
 **Gherkin**: Linguagem para definição de cenários
 **Langfuse**: Plataforma de observabilidade para LLMs
 **python-dotenv**: Gerenciamento de variáveis de ambiente

⚙️ Arquitetura da Solução

| Camada | Tecnologia | Responsabilidade |
| :--- | :--- | :--- |
| **Especificação** | Gherkin | Definição dos cenários de negócio. |
| **Orquestração** | Behave | Execução do ciclo de vida BDD. |
| **Core Engine** | Python 3 | Algoritmo de validação e parse de dados. |
| **Observabilidade** | Langfuse SDK | Captura de traces em tempo real. |
| **Data Source** | Base RAG Local | Fonte de dados do assistente (`manual_banco.txt`). |


 Executar suíte completa
 behave

 Gerar relatórios estruturados (JUnit/XML)
 behave --junit --junit-directory reports/

🚀 Estratégia de Testes
Os cenários cobrem operações bancárias comuns, incluindo:

Consulta de saldo.
Consulta de limite de crédito.
Consulta de fatura.
Informações de empréstimos.
Validação de respostas incorretas.
Tratamento de cenários de falha.

Além da validação funcional, cada execução mede a qualidade da resposta gerada pela IA.

Cenários de Teste - O projeto contém 8 cenários de teste:

1. **Consulta de saldo da conta corrente** - Valida saldo básico
2. **Consulta de saldo da conta poupança** - Valida saldo de poupança
3. **Consulta de saldo disponível com limite** - Valida saldo + limite
4. **Consulta de saldo total de todas as contas** - Valida saldo consolidado
5. **Consulta de saldo com informação incorreta** - Teste de falha
6. **Consulta de limite do cartão de crédito** - Valida limite do cartão
7. **Consulta de fatura atual do cartão** - Valida fatura do cartão
8. **Consulta de informações de empréstimo** - Valida dados de empréstimo

Status dos Testes

| Cenário | Status | Fidelidade |
|---------|--------|------------|
| Saldo Conta Corrente | ✅ Passou | 0.95 |
| Saldo Poupança | ✅ Passou | 0.92 |
| Saldo com Limite | ✅ Passou | 0.88 |
| Saldo Total | ✅ Passou | 0.91 |
| Saldo Incorreto | ✅ Passou (Falha Esperada) | 0.45 |
| Limite Cartão | ✅ Passou | 0.93 |
| Fatura Cartão | ✅ Passou | 0.90 |
| Empréstimo | ✅ Passou | 0.89 |

  **Total**: 8/8 cenários passando

  Evidências dos testes são armazenadas em:

 ` docs/evidencias/` - Screenshots, logs, artefatos
 ` docs/relatorios/` - Relatórios consolidados
  `reports/` - Relatórios gerados automaticamente pelo Behave


  📝  Rúbrica de Fidelidade
   A fidelidade das respostas da IA é calculada usando uma rúbrica matemática:
   Score de Fidelidade = (Precisão × 60%) + (Contexto × 25%) + (Formatação × 15%)

 **Precisão (60%)**: Proximidade do valor numérico extraído com o valor esperado
 **Contexto (25%)**: Presença de palavras-chave relevantes na resposta
 **Formatação (15%)**: Formatação correta (R$, vírgulas, pontos)
 **Critério de Aprovação**: Score > 0.80

🔍 Tracing com Langfuse
   Todos os testes registram traces no Langfuse para:
   Monitoramento de execução
   Análise de performance
   Debug de problemas
   Auditoria de resultados


  🐛 Troubleshooting

 Erro: ModuleNotFoundError: No module named 'langfuse.decorators'
**Solução**: O projeto usa o cliente padrão do Langfuse, não decorators. Verifique se está usando `from langfuse import Langfuse`.

Erro: FileNotFoundError: manual_banco.txt
**Solução**: Verifique se o arquivo `manual_banco.txt` está na raiz do projeto.

Erro: Fidelidade baixa (< 0.80)
**Solução**: Ajuste a rúbrica de fidelidade em `features/steps/steps.py` ou verifique a resposta da IA.




