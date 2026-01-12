from pydantic import BaseModel


class HealthCkeck(BaseModel):
    status: str = 'OK'


class Pizza(BaseModel):
    name: str
    price: float
    ingredients: list[str]


class PizzaDB(Pizza):
    id: int


class Pizzas(BaseModel):
    pizzas: list[PizzaDB]
