# dao = data access object
from establish_connection import get_sql_connection

def get_all_products(connection): # print all products in product table
    cursor = connection.cursor()
    query = ("SELECT product_id, name, products.unit_id, price_per_unit, units.unit_name FROM products INNER JOIN units ON products.unit_id = units.unit_id")
    cursor.execute(query)

    response = []
    for(product_id, name, unit_id, price_per_unit, unit_name) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name' : name,
                'unit_id' : unit_id,
                'price_per_unit' : price_per_unit,
                'unit_name' : unit_name
            }
        )

    return response


def insert_new_product(connection, product): # insert new product in product table
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, unit_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id): # delete product from product table
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    
    # print(get_all_products(connection))

    # print(insert_new_product(connection, {
    #     'product_name' : 'cabbage',
    #     'unit_id' : '2',
    #     'price_per_unit' : '10'
    # }))

    # print(delete_product(connection, 12))

    connection.close()