from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_health_retorna_ok():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_predict_com_dados_validos():
    payload = {
        "Country": "Brazil",
        "YearsCodePro": 5,
        "DevType": "Developer, full-stack",
        "EdLevel": "Bachelor's degree",
        "RemoteWork": "Remote",
        "OrgSize": "100 to 499 employees"
    }
    resposta = client.post("/predict", json=payload)
    assert resposta.status_code == 200

    corpo = resposta.json()
    assert "salario_previsto_usd" in corpo
    assert corpo["salario_previsto_usd"] > 0


def test_predict_com_payload_incompleto():
    payload = {"Country": "Brazil"}
    resposta = client.post("/predict", json=payload)
    assert resposta.status_code == 422


def test_predict_com_experiencia_extrema():
    payload = {
        "Country": "Brazil",
        "YearsCodePro": 60,
        "DevType": "Developer, full-stack",
        "EdLevel": "Bachelor's degree",
        "RemoteWork": "Remote",
        "OrgSize": "100 to 499 employees"
    }
    resposta = client.post("/predict", json=payload)
    assert resposta.status_code == 200
    assert resposta.json()["salario_previsto_usd"] > 0