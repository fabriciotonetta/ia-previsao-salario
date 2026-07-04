from pydantic import BaseModel

class DadosEntrada(BaseModel):
    Country: str
    YearsCodePro: float
    DevType: str
    EdLevel: str
    RemoteWork: str
    OrgSize: str

class RespostaPrevisao(BaseModel):
    salario_previsto_usd: float
    moeda: str = "USD"