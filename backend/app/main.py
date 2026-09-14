from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.routers import contact, pages

app = FastAPI(
    title=f"{settings.APP_NAME} — {settings.APP_TAGLINE}",
    description="Website institucional de consultoria de segurança ofensiva para ambientes OT/SCADA.",
    version="1.0.0",
    docs_url="/api/docs",
)

app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))

app.include_router(pages.router)
app.include_router(contact.router)


@app.exception_handler(404)
async def pagina_nao_encontrada(request: Request, exc):
    if request.url.path.startswith("/api"):
        return JSONResponse(status_code=404, content={"detail": "Recurso não encontrado."})
    return templates.TemplateResponse(
        request,
        "404.html",
        {"app_name": settings.APP_NAME, "app_tagline": settings.APP_TAGLINE, "active_page": None},
        status_code=404,
    )
