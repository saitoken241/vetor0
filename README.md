# VETOR0

Website institucional desenvolvido como projeto acadêmico para uma consultoria fictícia de segurança ofensiva em ambientes OT e SCADA.

O site apresenta serviços de pentest industrial, red team, avaliação de arquitetura e treinamento. A aplicação é demonstrativa e não realiza testes em ambientes industriais reais.

## Escopo

- Redes industriais, sistemas SCADA, PLCs, HMIs e estações de engenharia
- Avaliação ofensiva controlada e simulação de adversários
- Referências técnicas: ISA/IEC 62443, NIST SP 800-82 e MITRE ATT&CK for ICS
- Formulário institucional para solicitação de contato

Qualquer atividade de segurança ofensiva exige autorização formal, escopo definido, janela de execução e regras de interrupção.

## Tecnologias

- Python 3.11 ou superior
- FastAPI
- Jinja2 para renderização das páginas
- Pydantic 2 para validação dos dados
- HTML, CSS e JavaScript sem framework
- pytest e httpx para testes

## Organização

```text
.
├── backend/
│   ├── app/
│   │   ├── core/config.py       Configurações e caminhos
│   │   ├── routers/pages.py     Páginas HTML
│   │   ├── routers/contact.py   API de contato e healthcheck
│   │   ├── schemas/contact.py   Modelo de validação do formulário
│   │   ├── services/leads.py    Persistência dos contatos
│   │   └── main.py              Aplicação FastAPI
│   └── tests/                   Testes da aplicação
├── frontend/
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/main.js
│   │   └── img/
│   └── templates/               Templates Jinja2
├── data/                        Dados locais do formulário
├── requirements.txt
├── run.py
└── README.md
```

## Execução local

### Windows CMD

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
python run.py
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

O servidor ficará disponível em `http://127.0.0.1:8000`.

Também é possível iniciar o Uvicorn diretamente:

```bash
uvicorn app.main:app --reload --app-dir backend
```

## Rotas

| Método | Rota | Função |
| --- | --- | --- |
| GET | `/` | Página inicial |
| GET | `/servicos` | Serviços oferecidos |
| GET | `/sobre` | Informações institucionais |
| GET | `/contato` | Formulário de contato |
| GET | `/api/health` | Verificação da API |
| POST | `/api/contato` | Validação e registro de uma mensagem |
| GET | `/api/docs` | Documentação OpenAPI do FastAPI |

## Formulário de contato

O endpoint `POST /api/contato` recebe JSON com os campos abaixo:

```json
{
  "nome": "Nome da pessoa",
  "email": "pessoa@empresa.com",
  "empresa": "Empresa",
  "telefone": "(11) 90000-0000",
  "assunto": "pentest",
  "mensagem": "Descrição da solicitação",
  "consentimento": true
}
```

Os assuntos aceitos são `pentest`, `red-team`, `conformidade`, `treinamento` e `outro`. As mensagens válidas são salvas em `data/leads.json`. Esse arquivo é ignorado pelo Git e o projeto não possui integração de envio de e-mail.

## Testes

```bash
pytest backend/tests -v
```

Os testes cobrem as páginas principais, o healthcheck e as validações do formulário.

## Configuração

- `APP_NAME` em `backend/app/core/config.py` define o nome exibido pela aplicação. O valor padrão é `VETOR0`.
- As cores e dimensões do layout ficam nas variáveis `:root` de `frontend/static/css/style.css`.
- O conteúdo das páginas fica em `frontend/templates/`.
- Configurações locais podem ser fornecidas por um arquivo `.env`, que não deve ser versionado.

## Limitações

Este repositório contém apenas o site institucional e uma API simples para o formulário. Não inclui ferramentas de exploração, integração com e-mail, banco de dados de produção, autenticação de usuários ou monitoramento de ambientes OT.
