# Projeto de Automação QA Sênior - Assistente de IA Bancário

Este projeto implementa uma suite de testes automatizados para validar um Assistente de IA Bancário usando Gherkin (BDD), Playwright, Langfuse e uma rúbrica matemática de fidelidade (faithfulness).

## 📋 Estrutura do Projeto

```
.
├── manual_banco.txt              # Base de conhecimento RAG para a IA
├── requirements.txt              # Dependências Python
├── features/
│   ├── ia_bancaria.feature       # Cenários Gherkin em português
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

## 📦 Instalação

### 1. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Instalar browsers do Playwright

```bash
playwright install chromium
```

## 🔧 Configuração

### Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` ou exporte as variáveis:

```bash
export LANGFUSE_PUBLIC_KEY="sua-chave-publica"
export LANGFUSE_SECRET_KEY="sua-chave-secreta"
export LANGFUSE_HOST="https://cloud.langfuse.com"
```

**Nota**: Se não configurar, o projeto usará valores padrão e simulará as respostas da IA.

## 🏃 Executar os Testes

### Executar todos os cenários

```bash
behave
```

### Executar cenário específico

```bash
behave features/ia_bancaria.feature:5
```

### Executar com formato específico

```bash
behave --format=pretty
behave --format=json
behave --format=html
```

### Executar em modo headless (padrão)

```bash
behave
```

### Executar com browser visível (para debug)

Edite o arquivo `features/steps.py` e altere:
```python
browser = context_data["playwright"].chromium.launch(headless=False)
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

Para visualizar os traces, acesse seu dashboard no Langfuse.

## 🧪 Simulação vs Produção

O projeto está configurado em modo de simulação por padrão. Para usar com uma IA real:

1. Substitua a função `simular_resposta_ia()` em `features/steps.py` por chamadas reais à API da sua LLM
2. Configure as credenciais corretas do Langfuse
3. Atualize a URL da aplicação bancária nos steps

## 📂 Arquivo manual_banco.txt

Este arquivo contém a base de conhecimento RAG usada pela IA, incluindo:
- Informações de contas e saldos
- Tarifas e taxas
- Limites de transferência
- Informações de cartão de crédito
- Histórico de transações
- Empréstimos e financiamentos
- Políticas do banco

## 🐛 Debug

### Ver logs detalhados

```bash
behave -v
behave --no-capture
```

### Executar com breakpoint

Adicione `import pdb; pdb.set_trace()` no step desejado.

### Verificar instalação

```bash
python -c "import playwright; print(playwright.__version__)"
python -c "import langfuse; print(langfuse.__version__)"
python -c "import behave; print(behave.__version__)"
```

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

- Nunca commit credenciais reais no código
- Use variáveis de ambiente para chaves de API
- O arquivo `.env` deve estar no `.gitignore`

## 🤝 Contribuindo

1. Adicione novos cenários no arquivo `features/ia_bancaria.feature`
2. Implemente os steps correspondentes em `features/steps.py`
3. Atualize o `manual_banco.txt` se necessário
4. Execute os testes para validar

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique a documentação do [Behave](https://behave.readthedocs.io/)
- Verifique a documentação do [Playwright](https://playwright.dev/python/)
- Verifique a documentação do [Langfuse](https://langfuse.com/docs)

## ✅ Checklist antes de rodar

- [ ] Python 3.8+ instalado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Playwright browsers instalados (`playwright install chromium`)
- [ ] Arquivo `manual_banco.txt` presente
- [ ] Variáveis de ambiente configuradas (opcional)

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

## 📄 Licença

Este projeto é para fins educacionais e de demonstração.
