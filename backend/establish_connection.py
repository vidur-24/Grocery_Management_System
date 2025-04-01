import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='1010',
                    database='grocery_store'
                )

    return __cnx