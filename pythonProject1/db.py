import psycopg2
from config import *


def truncate():
    connection = connect()
    p_insert = '''TRUNCATE TABLE PERSON CASCADE;'''
    cursor = connection.cursor()
    cursor.execute(p_insert)
    connection.commit()


def connect():
    connection = psycopg2.connect(user=DB_user,
                                  password=DB_pas,
                                  host=DB_host,
                                  port=DB_port,
                                  database=DB_db)

    return connection


def disconnect(connection):
    connection.commit()
    connection.close()


def insert_person(message, connection):
    p_insert = '''INSERT INTO PERSON (PERSON_ID, REIT, ACTIVITY) VALUES (%s, %s, %s)'''
    ins = (message.from_user.id, 0, 0)
    cursor = connection.cursor()
    cursor.execute(p_insert, ins)
    connection.commit()


def insert_joke(message, connection):
    cursor = connection.cursor()
    p_insert = '''INSERT INTO JOKES (JOKE, PERSON_ID) VALUES (%s, %s)'''
    ins = (message.text, message.from_user.id)
    cursor.execute(p_insert, ins)
    connection.commit()


def insert(message):
    connection = connect()
    cursor = connection.cursor()
    p_ask = 'SELECT * FROM PERSON WHERE PERSON_ID=%s'
    ask = [message.from_user.id]
    cursor.execute(p_ask, ask)
    ans = cursor.fetchall()
    if len(ans) == 0:
        print("Add new person. ID =", message.from_user.id)
        insert_person(message, connection)
    insert_joke(message, connection)
    disconnect(connection)
