# Browser Use 🤖

## Descrição
Este projeto utiliza a biblioteca Browser Use para automatizar interações em navegadores de forma inteligente.

## Funcionalidades 📚

Execução Autônoma de Passos: Realiza navegação e ações definidas automaticamente.
Validações Automáticas: Verifica se elementos e conteúdos atendem aos critérios esperados.
Coleta de Evidências: Gera capturas de tela (PNG) e um GIF da sessão para auditoria.
Relatório Estruturado: Registra resultados, validações e caminhos das evidências em arquivo organizado.

## Pré-requisitos ⚙️
Para executar o projeto, você precisará de:

- Python 3.12 a 3.14
- `python-dotenv`
- `browser-use`
- `openai` (opcional, necessário se você utilizar modelos OpenAI)

Você pode instalar as dependências necessárias em um ambiente virtual:

## Como Executar 🚀

```bash

# 1. Clone o repositório e entre na pasta do projeto:
git clone https://github.com/emiliamariaa9933/auto-browser-use.git
cd auto-browser-use

# 2. Crie e ative um ambiente virtual:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 3. Instale as dependências:
pip install -r requirements.txt

# 4. Execute o projeto:
python agents/auto-browser-use.py