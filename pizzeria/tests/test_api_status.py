from http import HTTPStatus


def test_api_status_deve_retornar_ok(client):
    response = client.get('/api/status')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'status': 'OK'}
