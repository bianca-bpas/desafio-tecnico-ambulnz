from pydantic import BaseModel


class HealthCkeck(BaseModel):
    status: str = 'OK'

class Pizza(BaseModel):
    name: str
    price: int
    ingredients: list[str]