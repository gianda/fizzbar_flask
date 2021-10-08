from flask import Flask, jsonify, request
from models import MessageModel
import status


class FizzBar:
    def __init__(self):
        self.ingredients = {'latte': {'prezzo': 1, 'unita': 'cl'},
                            'caffe': {'prezzo': 20, 'unita': 'g'},
                            'acqua': {'prezzo': 0.5, 'unita': 'cl'},
                            'the': {'prezzo': 15, 'unita': 'g'},
                            }

        self.products_recipes = {'espresso': {'caffe': 3, 'acqua': 10},
                                 'americano': {'caffe': 3, 'acqua': 30},
                                 'the nero': {'the': 3, 'acqua': 30},
                                 'cappuccino': {'caffe': 3, 'acqua': 10, 'latte': 20},
                                 'macchiato': {'caffe': 3, 'acqua': 10, 'latte': 10},
                                 }

    def product_exists(self, product_name):
        return product_name in self.products_recipes.keys()

    def list_product_exists(self, list_products):
        return all(product in self.products_recipes.keys() for product in list_products)

    def calculate_price(self, product_name):
        if not self.product_exists(product_name):
            raise Exception('Product {} does not exist!'.format(product_name))
        recipe = self.products_recipes[product_name].items()
        price = 0
        for ingredient, quantity in recipe:
            price += quantity * self.ingredients[ingredient]['prezzo']
        return {product_name: price}

    def list_products(self, cart_list=None):
        if cart_list is None:
            cart_list = self.products_recipes.keys()
        elif not self.list_product_exists(cart_list):
            raise Exception('One or more products in list do not exist!')
        prod_list = {}
        for product in cart_list:
            prod_list.update(self.calculate_price(product))
        return prod_list

    def get_checkout_price(self, cart_list):
        return sum(self.list_products(cart_list).values())


app = Flask(__name__)
bar = FizzBar()


@app.route('/api/products/')
def get_product_list():
    message = MessageModel(
        message='OK',
        response=bar.list_products(),
        status=status.HTTP_200_OK
    )
    resp = jsonify(message.serialize())
    return resp


@app.route('/api/checkout/', methods=['POST'])
def post_checkout():
    order_list = request.get_json()
    # result = all(elem in bar.products_recipes.keys() for elem in order_list['data'])
    # if not result:
    #   abort(status.HTTP_404_NOT_FOUND, description="Beverage list is not correct")
    try:
        order_price = bar.get_checkout_price(order_list['data'])
        message = MessageModel(
            message='OK',
            response=order_price,
            status=status.HTTP_200_OK
        )
        resp = jsonify(message.serialize())
        return resp
    except Exception as e:
        return {'error': str(e)}, 404
        # abort(status.HTTP_404_NOT_FOUND, description=str(e))


if __name__ == '__main__':
    app.run(debug=True)
