from fastapi import FastAPI

from pizzeria.leitura_pizzas_json import obter_pizzas
from pizzeria.schemas import HealthCkeck, Pizzas

app = FastAPI(title='Pizzeria API')

pizza_database = obter_pizzas('pizzeria/data/example-pizzas.json')


@app.get('/api/status', response_model=HealthCkeck)
def get_api_status():
    return HealthCkeck(status='OK')


@app.get('/api/pizzas', response_model=Pizzas)
def read_pizzas():
    return {'pizzas': pizza_database}
