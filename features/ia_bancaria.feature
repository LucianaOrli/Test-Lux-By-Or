# language: pt
Funcionalidade: Assistente de IA Bancário - Consulta de Saldo com RAG

  Como cliente do banco
  Quero consultar meu saldo através do assistente de IA
  Para obter informações precisas sobre minhas contas baseadas no manual do banco

  Cenário: Consulta de saldo da conta corrente
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações da conta corrente do cliente João Silva
    Quando eu pergunto ao assistente "Qual é o saldo da minha conta corrente?"
    Então a IA deve responder com o saldo correto de R$ 5.450,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de saldo da conta poupança
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações da conta poupança do cliente João Silva
    Quando eu pergunto ao assistente "Qual é o saldo da minha poupança?"
    Então a IA deve responder com o saldo correto de R$ 12.300,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de saldo disponível com limite
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações sobre o limite de cheque especial
    Quando eu pergunto ao assistente "Qual é o saldo disponível incluindo o limite?"
    Então a IA deve responder com o saldo disponível de R$ 7.450,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de saldo total de todas as contas
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações de todas as contas do cliente
    Quando eu pergunto ao assistente "Qual é o saldo total de todas as minhas contas?"
    Então a IA deve responder com o saldo total de R$ 42.750,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de saldo com informação incorreta
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações da conta corrente do cliente João Silva
    E a IA responder com um valor diferente de R$ 5.450,00
    Então o teste deve falhar
    E a fidelidade deve ser menor ou igual a 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de limite do cartão de crédito
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações do cartão de crédito do cliente
    Quando eu pergunto ao assistente "Qual é o limite disponível do meu cartão de crédito?"
    Então a IA deve responder com o limite de R$ 15.000,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de fatura atual do cartão
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações do cartão de crédito do cliente
    Quando eu pergunto ao assistente "Qual é o valor da minha fatura atual do cartão?"
    Então a IA deve responder com o valor de R$ 3.450,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse

  Cenário: Consulta de informações de empréstimo
    Dado que o assistente de IA está disponível
    E o manual do banco contém informações de empréstimo do cliente
    Quando eu pergunto ao assistente "Qual é o valor devido do meu empréstimo pessoal?"
    Então a IA deve responder com o valor devido de R$ 15.500,00
    E a resposta deve ter fidelidade maior que 0.80
    E o trace da execução deve ser registrado no Langfuse
