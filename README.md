# Organizador de Estudos CLI

**Link do Repositório (Deploy CLI):** https://github.com/miguelDiniz-dev/estudo-organizer

**Versão:** 2.0.0
**Autor:** Miguel Oliveira Diniz Silva Ferreira

## O Problema Real
Muitos estudantes têm dificuldade de visualizar e organizar as horas que precisam dedicar a cada disciplina. Este projeto resolve essa dor oferecendo uma interface simples de linha de comando (CLI) para registrar matérias e planejar as horas de estudo.

## Funcionalidades Principais
- Consumo de API Pública para exibir dicas de estudo motivacionais.
- Adicionar uma nova matéria e horas de estudo.
- Listar o plano de estudos cadastrado.
## Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Testes:** `pytest`
- **Linting:** `ruff`
- **CI/CD:** GitHub Actions

## Como Instalar e Executar
1. Clone este repositório:
   `git clone https://github.com/miguelDiniz-dev/estudo-organizer.git`
2. Crie e ative o ambiente virtual:
   `python -m venv venv`
   *(Windows: `.\venv\Scripts\activate` | Mac/Linux: `source venv/bin/activate`)*
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Execute a aplicação:
   `python src/main.py`

## Como rodar os Testes e o Linting
Para verificar a qualidade do código: `ruff check .`
Para rodar os testes: `pytest`