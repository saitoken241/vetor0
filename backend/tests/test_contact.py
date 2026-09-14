from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

PAYLOAD_VALIDO = {
    "nome": "Aluna Teste",
    "email": "aluna@exemplo.com",
    "empresa": "Universidade Federal",
    "telefone": "(11) 90000-0000",
    "assunto": "pentest",
    "mensagem": "Gostaríamos de um orçamento para avaliação ofensiva da nossa rede OT.",
    "consentimento": True,
}


def test_contato_aceita_payload_valido(tmp_path, monkeypatch):
    monkeypatch.setattr("app.services.leads.LEADS_FILE", tmp_path / "leads.json")
    resposta = client.post("/api/contato", json=PAYLOAD_VALIDO)
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["ok"] is True
    assert corpo["protocolo"].startswith("V0-")


def test_contato_recusa_sem_consentimento(tmp_path, monkeypatch):
    monkeypatch.setattr("app.services.leads.LEADS_FILE", tmp_path / "leads.json")
    payload = {**PAYLOAD_VALIDO, "consentimento": False}
    resposta = client.post("/api/contato", json=payload)
    assert resposta.status_code == 422


def test_contato_recusa_email_invalido(tmp_path, monkeypatch):
    monkeypatch.setattr("app.services.leads.LEADS_FILE", tmp_path / "leads.json")
    payload = {**PAYLOAD_VALIDO, "email": "invalido"}
    resposta = client.post("/api/contato", json=payload)
    assert resposta.status_code == 422


def test_contato_recusa_assunto_invalido(tmp_path, monkeypatch):
    monkeypatch.setattr("app.services.leads.LEADS_FILE", tmp_path / "leads.json")
    payload = {**PAYLOAD_VALIDO, "assunto": "hackear-tudo"}
    resposta = client.post("/api/contato", json=payload)
    assert resposta.status_code == 422
