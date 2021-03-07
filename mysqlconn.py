import mysql.connector
from mysql.connector import Error

def getconn():
    # try:
    connection_config_dict = {
        'user': 'root',
        'password': 'root1234',
        'host': '127.0.0.1',
        'database': 'stockmarketdata',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)
    return connection

def mysqlaction(action, data):
    try:
        connection = getconn()
        if connection.is_connected():
            if action == 1 and data == []:
                cursor = connection.cursor()
                cursor.execute("show tables;")
                record = cursor.fetchall()
                print("Tables in current database: ", record)
            elif action == 2 and len(data) > 0:
                cursor = connection.cursor()
                cursor.execute('insert into historicalstockquotes(id, stocksymbol) values(1, ' + str(data[0]) + ');')
                cursor.execute("select * from historicalstockquotes;")
                record = cursor.fetchall()
                print("Results of query: ", record)
            else:
                print("invalid option or data...")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


mysqlaction(2,['LT Eq'])
