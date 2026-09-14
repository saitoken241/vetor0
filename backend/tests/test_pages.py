from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_retorna_200():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert "VETOR0" in resposta.text


def test_paginas_principais_retornam_200():
    for rota in ("/servicos", "/sobre", "/contato"):
        resposta = client.get(rota)
        assert resposta.status_code == 200


def test_rota_inexistente_retorna_404():
    resposta = client.get("/pagina-que-nao-existe")
    assert resposta.status_code == 404


def test_healthcheck():
    resposta = client.get("/api/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok", "service": "vetor0-api"}
