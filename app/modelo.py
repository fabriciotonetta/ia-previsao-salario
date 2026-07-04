import joblib
import pandas as pd

modelo = joblib.load("modelos/modelo_salario.pkl")
colunas_modelo = joblib.load("modelos/colunas_modelo.pkl")

def preparar_dados(dados: dict) -> pd.DataFrame:
    df_entrada = pd.DataFrame([dados])
    df_codificado = pd.get_dummies(df_entrada)
    df_final = df_codificado.reindex(columns=colunas_modelo, fill_value=0)
    return df_final

def prever_salario(dados: dict) -> float:
    df_preparado = preparar_dados(dados)
    previsao = modelo.predict(df_preparado)[0]
    return float(previsao)