from fastapi import FastAPI
from embrapa import Embrapa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou coloque o domínio do Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/" , tags=["Rota_teste"])
def read_root():
    return {"mensagem": "API Embrapa"}

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
def importacao_vinhos_de_mesa():
    s = Embrapa()
    dados = s.importacao_vinhos_de_mesa()
    return {"Importacao vinhos de mesa": dados}

@app.get('/importacao/espumantes', tags=["Importação"])
def importacao_espumantes():
    s = Embrapa()
    dados = s.importacao_espumantes()
    return {"Importacao vinhos de mesa": dados}

@app.get('/importacao/uvas_frescas', tags=["Importação"])
def importacao_uvas_frescas():
    s = Embrapa()
    dados = s.importacao_uvas_frescas()
    return {"Importacao uvas frescas": dados}

@app.get('/importacao/uvas_passas', tags=["Importação"])
def importacao_uvas_passas():
    s = Embrapa()
    dados = s.importacao_uvas_passas()
    return {"Importacao uvas_passas": dados}

@app.get('/importacao/suco_de_uvas', tags=["Importação"])
def importacao_suco_de_uva():
    s = Embrapa()
    dados = s.importacao_suco_de_uva()
    return {"Importacao suco de uva": dados}

@app.get('/exportacao/vinho_de_mesa', tags=["Exportação"])
def exportacao_vinho_de_mesa():
    s = Embrapa()
    dados = s.exportacao_suco_de_uva()
    return {"Exportacao suco de uva": dados}

@app.get('/exportacao/espumantes', tags=["Exportação"])
def exportacao_espumantes():
    s = Embrapa()
    dados = s.exportacao_espumantes()
    return {"Exportação espumantes:": dados}

@app.get('/exportacao/uvas_frescas', tags=["Exportação"])
def exportacao_uvas_frescas():
    s = Embrapa()
    dados = s.exportacao_uvas_frescas()
    return {"Exportação uvas frescas": dados}

@app.get('/exportacao/suco_de_uva', tags=["Exportação"])
def exportacao_suco_de_uva():
    s = Embrapa()
    dados = s.exportacao_suco_de_uva()
    return {"Exportação suco de uva": dados}




