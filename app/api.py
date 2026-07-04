from fastapi import FastAPI
from app.esquemas import DadosEntrada, RespostaPrevisao
from app.modelo import prever_salario

app = FastAPI(
    title="IA Previsão Salário",
    description="API para previsão de salário de profissionais de TI, com base em dados da Stack Overflow Developer Survey 2024.",
    version="1.0.0"
)

@app.get("/health")
def verificar_saude():
    return {"status": "ok"}

@app.post("/predict", response_model=RespostaPrevisao)
def prever(dados: DadosEntrada):
    dados_dict = dados.model_dump()
    salario = prever_salario(dados_dict)
    return RespostaPrevisao(salario_previsto_usd=round(salario, 2))