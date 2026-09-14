# VETOR0 (Vetor Zero) · Consultoria de Segurança Ofensiva OT/SCADA

Website institucional da **Vetor Zero**, consultoria fictícia de **segurança cibernética ofensiva para ambientes de Tecnologia da Operação (OT)** — redes industriais, SCADA, PLCs, HMIs e sistemas ciberfísicos. Projeto de faculdade inspirado em portais como [TI Safe](https://tisafe.com/).

> ⚠️ Conteúdo educacional. Descreve serviços de pentest/red team que, na prática, exigem autorização formal, contrato e regras de engagement rigorosas.

## Stack

- **Backend:** Python 3.11+ · FastAPI · Jinja2 (SSR) · Pydantic
- **Frontend:** HTML5 · CSS3 · JavaScript (vanilla)
- **Testes:** pytest + httpx

## Estrutura do projeto

```
.
├── backend/
│   ├── app/
│   │   ├── main.py            # Fábrica da aplicação FastAPI
│   │   ├── core/
│   │   │   └── config.py      # Configurações (env, paths)
│   │   ├── routers/
│   │   │   ├── pages.py       # Rotas das páginas (SSR via Jinja2)
│   │   │   └── contact.py     # POST /api/contato (form de contato)
│   │   ├── schemas/
│   │   │   └── contact.py     # Modelos Pydantic de validação
│   │   └── services/
│   │       └── leads.py       # Persistência dos leads (data/leads.json)
│   └── tests/                 # Testes automatizados (pytest)
├── frontend/
│   ├── static/
│   │   ├── css/style.css      # Design system completo (dark/industrial)
│   │   ├── js/main.js         # Menu, animações, terminal, formulário
│   │   └── img/               # Imagens e favicon
│   └── templates/             # Páginas Jinja2 (base + páginas)
├── data/                      # Saída dos formulários (gitignored)
├── requirements.txt
└── README.md
```

## Como rodar

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Subir o servidor de desenvolvimento
python run.py
# ou: uvicorn app.main:app --reload --app-dir backend

# 4. Acessar
# http://127.0.0.1:8000
```

## Rotas

| Método | Rota            | Descrição                                  |
|--------|-----------------|--------------------------------------------|
| GET    | `/`             | Página inicial (hero, serviços, metodologia)|
| GET    | `/servicos`     | Portfólio detalhado de serviços            |
| GET    | `/sobre`        | Quem somos / equipe                        |
| GET    | `/contato`      | Formulário de contato                      |
| GET    | `/api/health`   | Healthcheck da API                         |
| POST   | `/api/contato`  | Recebe e valida o formulário (JSON)        |

## Testes

```bash
pytest backend/tests -v
```

## Personalizar

- **Nome da consultoria:** troque `APP_NAME` em `backend/app/core/config.py` e o texto do logo em `frontend/templates/base.html`. (Padrão: VETOR0)
- **Cores:** edite as variáveis CSS em `frontend/static/css/style.css` (`:root`).
- **Conteúdo:** cada página vive em `frontend/templates/*.html`.
