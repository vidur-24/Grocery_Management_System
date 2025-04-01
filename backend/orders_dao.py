from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders(customer_name, total, datetime) VALUES(%s, %s, %s)")
    order_data = (order['customer_name'], order['total'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_detail_query = ("INSERT INTO order_details(order_id, product_id, quantity, total_price) VALUES(%s, %s, %s, %s)")
    order_detail_data = []
    for order_detail_record in order['order_details']:
        order_detail_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_detail_query, order_detail_data)

    connection.commit()

    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM orders"
    cursor.execute(query)

    response = []
    for(order_id, customer_name, total, datetime) in cursor:
        response.append({
            'order_id' : order_id,
            'customer_name' : customer_name,
            'total' : total,
            'datetime' : datetime
        })
        
    return response

if __name__ == '__main__':
    from establish_connection import get_sql_connection
    connection = get_sql_connection()
    
    # print(insert_order(connection, {
    #     'customer_name' : 'Hulk',
    #     'total' : '600',
    #     'order_details' : [
    #         {
    #             'product_id' : 1,
    #             'quantity' : 2,
    #             'total_price' : 50
    #         },
    #         {
    #             'product_id' : 3,
    #             'quantity' : 1,
    #             'total_price' : 30
    #         }
    #     ]
    # }))

    print(get_all_orders(connection))