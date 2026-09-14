from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.schemas.contact import ContactMessage
from app.services import leads

router = APIRouter(prefix="/api", tags=["contato"])


@router.get("/health")
async def health():
    return {"status": "ok", "service": "vetor0-api"}


@router.post("/contato", status_code=status.HTTP_201_CREATED)
async def enviar_contato(mensagem: ContactMessage):
    registro = leads.save_lead(mensagem)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "ok": True,
            "message": "Mensagem recebida. Nossa equipe responderá em até 1 dia útil.",
            "protocolo": registro["protocolo"],
        },
    )
