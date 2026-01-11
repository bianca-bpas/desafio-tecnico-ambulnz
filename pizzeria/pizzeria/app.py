from fastapi import FastAPI

from pizzeria.schemas import HealthCkeck

app = FastAPI(title='Pizzeria API')


@app.get('/api/status', response_model=HealthCkeck)
def get_api_status():
    return HealthCkeck(status='OK')
