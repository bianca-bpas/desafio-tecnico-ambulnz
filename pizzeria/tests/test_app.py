from http import HTTPStatus


def test_api_status_deve_retornar_ok(client):
    response = client.get('/api/status')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'status': 'OK'}


def test_api_get_pizzas_deve_retornar_pizzas_do_json(client):
    response = client.get('/api/pizzas')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'pizzas': [
            {
                'id': 0,
                'name': 'Margherita',
                'price': 5.0,
                'ingredients': ['tomato', 'mozzarella'],
            },
            {
                'id': 1,
                'name': 'Bufala',
                'price': 6.0,
                'ingredients': ['tomato', 'mozarella di bufala'],
            },
            {
                'id': 2,
                'name': 'Romana',
                'price': 5.0,
                'ingredients': [
                    'tomato',
                    'mozzarella',
                    'anchovies',
                    'oregano',
                    'oil',
                ],
            },
            {
                'id': 3,
                'name': 'Diavola',
                'price': 7.5,
                'ingredients': ['tomato', 'mozzarella', 'spicy salami'],
            },
            {
                'id': 4,
                'name': 'Pizza Bianca',
                'price': 5.0,
                'ingredients': ['mozzarella', 'oregano'],
            },
        ]
    }
