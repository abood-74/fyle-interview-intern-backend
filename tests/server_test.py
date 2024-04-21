from core.libs import helpers


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'ready'
    assert 'time' in response.json