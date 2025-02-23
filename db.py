
import mysql.connector
import pymysql

def getpy_db_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='2004',
        database='clockmakers'
    )
    return conn
# Initialize MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2004",
        database="clockmakers"
    )
    return conn