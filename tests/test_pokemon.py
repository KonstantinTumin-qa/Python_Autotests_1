import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_by_level():

    '''
    KTI-1. Get trainers by level
    '''
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():

    '''
    KTI-2. Get trainers by id
    '''
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 142}, timeout=5)
    assert response.json()['trainer_name'] == 'Test API Tumin'