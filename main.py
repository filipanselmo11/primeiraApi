from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco": 20, "quantidade": 3},
    3: {"item": "panela de pressao", "preco": 4.50, "quantidade": 2},
    4: {"item": "ventilador", "preco": 30, "quantidade": 10},
}

#REST API

@app.get('/')
def home():
    return {"Vendas": vendas ,"Tamanho": len(vendas)}

@app.get('/vendas/{id}')
def get_venda(id: int):
    if id in vendas:
        return vendas[id]
    else:
        return {"Erro": "Id da venda inexistente"}