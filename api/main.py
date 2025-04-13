from fastapi import FastAPI
from mangum import Mangum
  # ou apenas use direto se estiver no mesmo arquivo

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def home():
    return {"status": "ok"}

