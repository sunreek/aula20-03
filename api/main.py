from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    titulo="API do unipão"
    descrição="essa api serve para calcular a previsão de preço de uma ação na bolsa"
    docs_url='/docs'#habilitar o swagger
)

class InfoPrevisao(BaseModel):
    empresa: str
    volume:float
    prev_fecham:float

@app.get("/")
async def principal():
    return {"status" : true,
            "messagem": "serviço rodando"}


###***criando um post, porque vamos colocar itens, por isso é post (criar)***
@app.post("predict")
def previsoes(payload : InfoPrevisao):
    if InfoPrevisao.empresa == "aapl":
        w0, w1, w2 = [-15.36, 1.06, -3.25]
        previsao = w0 + w1 * InfoPrevisao.prev_fecham + w2 * InfoPrevisao.volume
    else
    previsao = 0

    return {"profesia": revisão}