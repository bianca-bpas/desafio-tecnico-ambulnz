import json
from pizzeria.schemas import Pizza, PizzaDB, Pizzas

def read_pizzas():
    with open('pizzeria/data/example-pizzas.json', 'r') as file:
        data = json.load(file)
        return data
    
def obter_pizzas():
    pizza_database = []
    
    data = read_pizzas()
    for index, pizza in enumerate(data):
        obj = Pizza(**pizza)
        pizza_db = PizzaDB(**obj.model_dump(), id=index)

        pizza_database.append(pizza_db)

    return pizza_database
