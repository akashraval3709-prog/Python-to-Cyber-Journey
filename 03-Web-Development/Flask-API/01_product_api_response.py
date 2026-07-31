from flask import Flask , jsonify

app = Flask(__name__)
product_database = {
        101: {
            "title": "Wireless Gaming Mouse",
            "price": 1499.50,
            "in_stock": True,
            "discount": 10.0,
            "tags": ("electronics", "accessories") 
        },
        102: {
            "title": "Mechanical Keyboard",
            "price": 3499.00,
            "in_stock": False,
            "discount": None,                   
            "tags": ["gaming", "keyboard"]
        },
        103: {
            "title": "USB-C Fast Charger",
            "price": 699.00,
            "in_stock": True,
            "discount": 5.5,
            "tags": ("mobile", "charger")
        }
    }


@app.route("/")
def home():
    return "Flask Product API is Running "
@app.route('/product/<int:product_id>',methods=["GET"])
def get_product(product_id):
    if product_id in product_database:
        proData = product_database[product_id]
        responce_data={
            'status' : 'success',
            'message':'product fond successfully',
            'data' : proData
        }
        return jsonify(responce_data),200
    else:
        responce_data={
            'status' : 'Error',
            'message' : 'product not found',
            'data' : None

        }
        return jsonify(responce_data),404



if __name__ == '__main__':
    app.run(debug=True)
