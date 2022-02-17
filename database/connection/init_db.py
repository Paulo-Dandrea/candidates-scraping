import os
from os.path import join, dirname
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import errorcode


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.getenv('HOST')
PASSWORD = os.environ.get("PASSWORD")
USER = os.environ.get("USER")


def db_init():
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
        )

        cursor = mydb.cursor()

        cursor.execute("DROP DATABASE IF EXISTS sample_university")
        cursor.execute("CREATE DATABASE sample_university")
        cursor.close()

        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="sample_university"
        )
        
        cursor = mydb.cursor()

        cursor.execute("DROP TABLE IF EXISTS candidates")
        # Score should be a float
        cursor.execute(
            "CREATE TABLE candidates (name VARCHAR(255), score VARCHAR(255), cpf VARCHAR(255))")
        cursor.close()

        return 'init database'

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print('err', err)
