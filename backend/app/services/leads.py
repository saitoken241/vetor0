import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from app.core.config import settings
from app.schemas.contact import ContactMessage

LEADS_FILE = settings.DATA_DIR / "leads.json"


def _write_leads(registros: list[dict]) -> None:
    LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)
    LEADS_FILE.write_text(
        json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_leads() -> list[dict]:
    if not LEADS_FILE.exists():
        return []
    return json.loads(LEADS_FILE.read_text(encoding="utf-8"))


def save_lead(mensagem: ContactMessage) -> dict:
    registro = {
        "id": str(uuid.uuid4()),
        "protocolo": datetime.now(timezone.utc).strftime("V0-%Y%m%d-%H%M%S"),
        "recebido_em": datetime.now(timezone.utc).isoformat(),
        **mensagem.model_dump(),
    }
    registros = load_leads()
    registros.append(registro)
    _write_leads(registros)
    return registro
