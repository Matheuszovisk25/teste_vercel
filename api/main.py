from testes.fast_api import FastAPI
from api.embrapa import Embrapa
from mangum import Mangum
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"mensagem": "API Embrapa rodando! Acesse /producao, /comercializacao etc."}

@app.get("/producao", tags=["Producao"])
def get_producao():
    s = Embrapa()
    dados = s.producao()
    return {"Producao Vinhos Embrapa - 2023": dados}

@app.get('/comercializacao', tags=["Comercializacao"])
def get_comercializacao():
    s = Embrapa()
    dados = s.comercializacao()
    return {"Comercializacao de vinhos - 2023": dados}

@app.get('/processamento/viniferas', tags=["Processamento"])
def get_processamento_viniferas():
    s = Embrapa()
    dados = s.processamento_viniferas()
    return {"Processamento de viniferas": dados}

@app.get('/processamento/americanas', tags=["Processamento"])
def get_processamento_americanas():
    s = Embrapa()
    dados = s.processamento_americanas_e_hibridas()
    return {"Processamento americanas e hibridas": dados}

@app.get('/processamento/uvas_de_mesa', tags=["Processamento"])
def get_processamento_uvas_de_mesa():
    s = Embrapa()
    dados = s.processamento_uvas_de_mesa()
    return {"Processamento uvas de mesa": dados}

@app.get('/importacao/vinhos_de_mesa', tags=["Importação"])
def get_importacao_vinhos_de_mesa():
    s = Embrapa()
    dados = s.importacao_espumantes()
    return {"importacao de vinhos de mesa": dados}


handler = Mangum(app)