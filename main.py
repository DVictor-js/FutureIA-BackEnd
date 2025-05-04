import pandas as pd
from fastapi import FastAPI, File, UploadFile
import plotly.express as px
from io import StringIO

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem:": "Api Funcionando"}

@app.post("/uploadfile/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        return {"Erro": "O Arquivo para upload deve ser .csv"}
    
    content = await file.read()
    try:
        df = pd.read_csv(StringIO(content.decode('utf-8')))
        return{
            "colunas": df.columns.tolist(),
            "linhas":len(df)
        }
    except Exception as e:
        return{"Error": f"Erro ao ler CSV:{str(e)}"}



