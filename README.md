# 🤖 Projeto de Automação QA Sênior - Assistente de IA Bancário

## 📋 Visão Geral

Projeto de automação de testes de nível Sênior para validação de um Assistente de IA Bancário utilizando RAG (Retrieval-Augmented Generation). O projeto utiliza Behavior-Driven Development (BDD) com Gherkin, Python, Behave e integração com Langfuse para tracing e observabilidade.

## 🎯 Objetivo

Validar as respostas do Assistente de IA Bancário garantindo:
- Precisão nas informações fornecidas
- Fidelidade das respostas baseada em rúbrica matemática
- Observabilidade através de traces no Langfuse
- Cobertura de cenários de sucesso e falha

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
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Behave**: Framework BDD para Python
- **Gherkin**: Linguagem para definição de cenários
- **Langfuse**: Plataforma de observabilidade para LLMs
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone <URL-DO-REPOSITORIO>
   cd Test-Lux-By-Or
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas credenciais do Langfuse
   ```

## 🚀 Execução dos Testes

### Executar todos os testes
```bash
behave
```

### Executar cenário específico
```bash
behave features/ia_bancaria.feature:8
```

### Executar com formato JSON
```bash
behave --format json.pretty --out reports/report.json
```

### Executar com formato HTML
```bash
behave --format html --out reports/report.html
```

## 📊 Cenários de Teste

O projeto contém 8 cenários de teste:

1. **Consulta de saldo da conta corrente** - Valida saldo básico
2. **Consulta de saldo da conta poupança** - Valida saldo de poupança
3. **Consulta de saldo disponível com limite** - Valida saldo + limite
4. **Consulta de saldo total de todas as contas** - Valida saldo consolidado
5. **Consulta de saldo com informação incorreta** - Teste de falha
6. **Consulta de limite do cartão de crédito** - Valida limite do cartão
7. **Consulta de fatura atual do cartão** - Valida fatura do cartão
8. **Consulta de informações de empréstimo** - Valida dados de empréstimo

## 🧮 Rúbrica de Fidelidade

A fidelidade das respostas da IA é calculada usando uma rúbrica matemática:

```
Score de Fidelidade = (Precisão × 60%) + (Contexto × 25%) + (Formatação × 15%)
```

- **Precisão (60%)**: Proximidade do valor numérico extraído com o valor esperado
- **Contexto (25%)**: Presença de palavras-chave relevantes na resposta
- **Formatação (15%)**: Formatação correta (R$, vírgulas, pontos)

**Critério de Aprovação**: Score > 0.80

## 🔍 Tracing com Langfuse

Todos os testes registram traces no Langfuse para:
- Monitoramento de execução
- Análise de performance
- Debug de problemas
- Auditoria de resultados

**Configuração**:
```python
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
```

## 📝 Evidências

As evidências dos testes são armazenadas em:
- `docs/evidencias/` - Screenshots, logs, artefatos
- `docs/relatorios/` - Relatórios consolidados
- `reports/` - Relatórios gerados automaticamente pelo Behave

## 🧪 Checklist Pré-Execução

Antes de executar os testes, verifique:

- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Variáveis de ambiente configuradas (`.env`)
- [ ] Arquivo `manual_banco.txt` presente na raiz
- [ ] Credenciais do Langfuse válidas
- [ ] Conexão com internet (para Langfuse)

## 🐛 Troubleshooting

### Erro: ModuleNotFoundError: No module named 'langfuse.decorators'
**Solução**: O projeto usa o cliente padrão do Langfuse, não decorators. Verifique se está usando `from langfuse import Langfuse`.

### Erro: FileNotFoundError: manual_banco.txt
**Solução**: Verifique se o arquivo `manual_banco.txt` está na raiz do projeto.

### Erro: Fidelidade baixa (< 0.80)
**Solução**: Ajuste a rúbrica de fidelidade em `features/steps/steps.py` ou verifique a resposta da IA.

## 📈 Status dos Testes

**Última Execução**: 17/06/2026

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

## 👥 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é para fins educacionais e de demonstração.

## 👤 Autor

**QA Sênior** - Automação de Testes com IA

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório.

---

**Última Atualização**: 17/06/2026
