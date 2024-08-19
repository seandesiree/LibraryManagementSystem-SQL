import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root', 
        password='evangelista4ever',
        host='localhost', 
        database='LibrarySystem'
        )
    if conn.is_connected():
            print('Connected to database.')
except Exception as e:
        print(f'Error: {e}')

        
        
    