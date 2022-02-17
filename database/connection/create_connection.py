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


def create_connection():
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="sample_university"
        )

        return cnx
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print('err', err)
