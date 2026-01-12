import json

from pizzeria.schemas import Pizza, PizzaDB


def read_pizzas(url):
    with open(url, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def obter_pizzas(url):
    pizza_database = []

    data = read_pizzas(url)
    for index, pizza in enumerate(data):
        obj = Pizza(**pizza)
        pizza_db = PizzaDB(**obj.model_dump(), id=index)

        pizza_database.append(pizza_db)

    return pizza_database
