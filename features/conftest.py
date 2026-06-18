"""
Arquivo de configuração do Behave para testes do Assistente de IA Bancário.
Este arquivo define hooks de before e after para setup e cleanup dos testes.
"""

from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import os


@fixture
def browser_playwright(context):
    """
    Fixture que inicializa o navegador Playwright antes dos testes.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context.browser = browser
        context.page = browser.new_page()
        yield context.page
        browser.close()


def before_all(context):
    """
    Hook executado antes de todos os cenários.
    Configura variáveis de ambiente e inicializa recursos globais.
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
    print(f"✅ Playwright pronto para uso")


def before_scenario(context, scenario):
    """
    Hook executado antes de cada cenário.
    Limpa o contexto e prepara o ambiente para o teste.
    """
    print(f"\n📋 Cenário: {scenario.name}")
    print("-" * 70)
    
    # Limpa dados do contexto
    context.ia_response = None
    context.faithfulness_score = None
    context.expected_value = None
    context.pergunta = None


def after_scenario(context, scenario):
    """
    Hook executado após cada cenário.
    Realiza cleanup e relata o status do teste.
    """
    print("-" * 70)
    
    if scenario.status == "passed":
        print(f"✅ CENÁRIO APROVADO: {scenario.name}")
        if hasattr(context, 'faithfulness_score') and context.faithfulness_score:
            print(f"   Score de Fidelidade: {context.faithfulness_score:.2f}")
    elif scenario.status == "failed":
        print(f"❌ CENÁRIO FALHOU: {scenario.name}")
        if hasattr(context, 'faithfulness_score') and context.faithfulness_score:
            print(f"   Score de Fidelidade: {context.faithfulness_score:.2f}")
    else:
        print(f"⚠️  CENÁRIO: {scenario.name} - Status: {scenario.status}")
    
    print()


def after_all(context):
    """
    Hook executado após todos os cenários.
    Realiza cleanup final e exibe resumo.
    """
    print("="*70)
    print("🏁 SUITE DE TESTES FINALIZADA")
    print("="*70)
    
    # Fecha o navegador se estiver aberto
    if hasattr(context, 'browser'):
        context.browser.close()
    
    print("✅ Cleanup realizado com sucesso")
