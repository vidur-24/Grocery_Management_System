from flask import Flask, request, jsonify, json
from establish_connection import get_sql_connection
import products_dao, units_dao, orders_dao
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
connection = get_sql_connection()

@app.route("/getProducts", methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getUnits", methods=['GET'])
def get_units():
    response = units_dao.get_units(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/deleteProduct", methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertProduct", methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id' : product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertOrder", methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id' : order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getAllOrders", methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(debug=True, port=5000)