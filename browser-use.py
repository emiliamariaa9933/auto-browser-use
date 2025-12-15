
from browser_use import Agent, Browser, ChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def wikipedia_flow():
    browser = Browser()
    llm = ChatOpenAI(model="openai/gpt-4o-mini", base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))

    task = """
    Objetivo: Navegar autonomamente na Wikipedia, buscar um termo, abrir um artigo, extrair texto e validar conteúdo, coletando evidências (prints PNG e GIF).

    Site alvo: https://pt.wikipedia.org/

    Passos:
    1) Acesse https://pt.wikipedia.org/.
       - Faça uma captura de tela (PNG) da seção.

    2) Localize o campo de busca (geralmente com placeholder 'Pesquisar na Wikipédia').
       - Clique no corpo da página para desfocar qualquer campo previamente focado.
       - Digite 'Selenium (software)' e pressione Enter para buscar.
       - Faça uma captura de tela (PNG) da seção.

    3) Clique no artigo 'Selenium (software)' em português.
       - Valide que o h1 contém 'Selenium (software)'.
       - Faça uma captura de tela (PNG) da seção.

    4) Role até a seção 'Uso em outros projetos' (se existir) e valide a presença da seção.
       - Caso não exista, faça scroll até a primeira seção disponível e registre o nome.
       - Faça uma captura de tela (PNG) da seção.

    5) Extraia o primeiro parágrafo introdutório.
       - Armazene como 'artigo_intro' e valide que contém 'Selenium'.
       - Faça uma captura de tela (PNG) do trecho do parágrafo.

    6) Relatório final:
       - Inclua 'titulo_pagina', 'url_pagina', 'artigo_intro', e 'validacoes' (status de cada validação).

    RESTRIÇÕES IMPORTANTES:
    - NUNCA digite nomes de arquivos, comandos ou textos de observação na interface da página (ex.: não digitar 'Generate GIF', 'screenshot1.png').
    - Aguarde carregamentos (use waits) e evite anúncios/links externos.

    CRITÉRIOS DE SUCESSO:
    - As validações de título (h1) e conteúdo ('Selenium' em 'artigo_intro') devem passar.
    - Uma vez atendidos os critérios, finalize a execução sem repetir ações.
    """

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        sensitive_data={},
        generate_gif=True
    )

    history = await agent.run()
    history.save_to_file("AgentHistory_Wikipedia.json")
    return history

if __name__ == "__main__":
    asyncio.run(wikipedia_flow())