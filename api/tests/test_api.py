import requests

prod_list = {"americano": 75.0,
             "cappuccino": 85.0,
             "espresso": 65.0,
             "macchiato": 75.0,
             "the nero": 60.0}

url = 'http://localhost:5000'


def test_correct_checkout():
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"data":["espresso","americano"]}'
    response = requests.post(url+'/api/checkout/', headers=headers, data=data)
    assert response.json()['message'] == 'OK'
    assert response.json()['response'] == 140
    assert response.json()['status'] == 200


def test_incorrect_checkout():
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"data":["espresso","beer"]}'
    response = requests.post(url+'/api/checkout/', headers=headers, data=data)
    assert response.status_code == 404
    assert response.json()['error'] == 'One or more products in list do not exist!'


def test_get_product_list():
    response = requests.get(url+'/api/products/')
    assert response.status_code == 200
    assert response.json()['response'] == prod_list
