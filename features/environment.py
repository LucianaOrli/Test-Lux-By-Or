"""
features/environment.py
Arquivo de configuração nativo do Behave para testes do Assistente de IA Bancário.
Define hooks de setup, cleanup e inicialização limpa do Playwright.
"""

import os
from playwright.sync_api import sync_playwright


def before_all(context):
    """
    Hook executado antes de todos os cenários.
    Configura variáveis de ambiente e inicializa o Playwright globalmente.
    """
    print("\n" + "="*70)
    print("🚀 INICIANDO SUITE DE TESTES - ASSISTENTE IA BANCÁRIO")
    print("="*70)
    
    # Configura variáveis de ambiente para Langfuse
    os.environ.setdefault("LANGFUSE_PUBLIC_KEY", "pk-lf-...")
    os.environ.setdefault("LANGFUSE_SECRET_KEY", "sk-lf-...")
    os.environ.setdefault("LANGFUSE_HOST", "https://cloud.langfuse.com")
    
    # Verifica se o manual do banco existe
    manual_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "manual_banco.txt")
    if not os.path.exists(manual_path):
        raise FileNotFoundError(f"Arquivo manual_banco.txt não encontrado em: {manual_path}")
    
    print(f"✅ Manual do banco encontrado: {manual_path}")
    print(f"✅ Langfuse configurado")

    # Inicialização correta e limpa do Playwright no contexto global do Behave
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()
    print(f"✅ Playwright pronto para uso (Headless: True)")


def before_scenario(context, scenario):
    """
    Hook executado antes de cada cenário.
    Limpa o contexto e prepara o ambiente para o teste.
    """
    print(f"\n📋 Cenário: {scenario.name}")
    print("-" * 70)
    
    # Limpa/Inicializa dados do contexto para evitar vazamento de escopo entre cenários
    context.ia_response = None
    context.faithfulness_score = None
    context.expected_value = None
    context.pergunta = None


def after_scenario(context, scenario):
    """
    Hook executado após cada cenário.
    Realiza cleanup de logs e relata o status do teste.
    """
    print("-" * 70)
    
    if scenario.status == "passed":
        print(f"✅ CENÁRIO APROVADO: {scenario.name}")
        if hasattr(context, 'faithfulness_score') and context.faithfulness_score is not None:
            print(f"   Score de Fidelidade: {context.faithfulness_score:.2f}")
    elif scenario.status == "failed":
        print(f"❌ CENÁRIO FALHOU: {scenario.name}")
        if hasattr(context, 'faithfulness_score') and context.faithfulness_score is not None:
            print(f"   Score de Fidelidade: {context.faithfulness_score:.2f}")
    else:
        print(f"⚠️  CENÁRIO: {scenario.name} - Status: {scenario.status}")
    print()


def after_all(context):
    """
    Hook executado após todos os cenários.
    Garante o encerramento seguro do browser e do processo do Playwright.
    """
    print("="*70)
    print("🏁 SUITE DE TESTES FINALIZADA")
    print("="*70)
    
    # Encerra os recursos do Playwright na ordem reversa de criação
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
        
    print("✅ Cleanup do Playwright e encerramento de processos concluídos")
