import csv
import mysql.connector
from mysql.connector import Error

db = {
    'host' : 'localhost',
    'user' : 'root',
    'database' : 'cafe_sql',
    'password' : ''
}

def conn(db):
    '''connect to database'''
    conn = None
    try:
        conn = mysql.connector.connect(**db);
        if conn.is_connected():
            print('Connect to mySQL database')
        data = []
        mycursor = conn.cursor()
        sql = "INSERT INTO data (id, source, title, created_at) VALUES (%s, %s, %s ,%s)"
        with open("GFG.csv") as my_file:
            csv_reader = csv.reader(my_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                data.append(tuple(row))
        mycursor.executemany(sql, data)
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            print("Closing database")
            conn.commit()
            conn.close()


def main():
    conn(db)

if __name__ == '__main__':
    main()