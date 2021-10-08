from api.app import app
import pytest

prod_list = {"americano": 75.0,
             "cappuccino": 85.0,
             "espresso": 65.0,
             "macchiato": 75.0,
             "the nero": 60.0}

bar = app.FizzBar()


def test_product_that_exists():
    assert bar.product_exists('espresso') is True


def test_product_that_not_exists():
    assert bar.product_exists('beer') is False


def test_list_product_that_exists():
    assert bar.list_product_exists(['espresso', 'americano']) is True


def test_list_product_that_not_exists():
    assert bar.list_product_exists(['espresso', 'beer']) is False


def test_espresso_price():
    assert bar.calculate_price('espresso') == {'espresso': 65}


def test_calculate_price_product_not_exist():
    with pytest.raises(Exception):
        bar.calculate_price('beer')


def test_all_products_price():
    assert bar.calculate_price('espresso') == {'espresso': 65}
    assert bar.calculate_price('americano') == {'americano': 75}
    assert bar.calculate_price('the nero') == {'the nero': 60}
    assert bar.calculate_price('cappuccino') == {'cappuccino': 85}
    assert bar.calculate_price('macchiato') == {'macchiato': 75}


def test_list_all_products():
    assert bar.list_products() == prod_list


def test_list_filtered_one_product():
    assert bar.list_products(['espresso']) == {'espresso': 65}


def test_list_filtered_two_product():
    assert bar.list_products(['espresso', 'americano']) == {'espresso': 65, 'americano': 75}


def test_list_filtered_error_product():
    with pytest.raises(Exception):
        bar.list_products(['beer'])


def test_checkout_price():
    assert bar.get_checkout_price(['espresso', 'americano']) == 140
