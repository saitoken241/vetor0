from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import settings

router = APIRouter()
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))


def _render(request: Request, template: str, **context) -> HTMLResponse:
    context.setdefault("app_name", settings.APP_NAME)
    context.setdefault("app_tagline", settings.APP_TAGLINE)
    return templates.TemplateResponse(request, template, context)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return _render(request, "index.html", active_page="home")


@router.get("/servicos", response_class=HTMLResponse)
async def servicos(request: Request):
    return _render(request, "servicos.html", active_page="servicos")


@router.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return _render(request, "sobre.html", active_page="sobre")


@router.get("/contato", response_class=HTMLResponse)
async def contato(request: Request):
    return _render(request, "contato.html", active_page="contato")
