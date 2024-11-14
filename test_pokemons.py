import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='a3531a460206f2a9f228ce44baa3171a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '8142'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["name"] == 'Mishka'


@pytest.mark.parametrize('key, value',[('name', 'Mishka'), ('trainer_id', TRAINER_ID), ('id', '132401')])
def test_parametrize(key, value):
        response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
        assert response_parametrize.json()["data"][0][key] == value