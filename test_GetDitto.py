import requests

api = f'https://pokeapi.co/api/v2/pokemon/ditto'

def test_get_id():
    res = requests.get(api)
    data = res.json()
    assert data['id'] == 132

def test_get_type():
    res = requests.get(api)
    data = res.json()
    for i in data['types']:
        assert i['type']['name'] == 'normal'

def test_get_name():
    res = requests.get(api)
    data = res.json()
    assert data['name'] == 'ditto'







