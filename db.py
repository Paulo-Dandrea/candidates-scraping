import json
import mysql.connector
from mysql.connector import errorcode


def get_candidates():
    try:
        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="sample_university"
        )

        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM candidates")

        # this will extract row headers
        row_headers = [x[0] for x in cursor.description]

        results = cursor.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()

        return json.dumps({'number_of_candidates': len(json_data), 'candidates': json_data})

    # Provavelmente tem uma forma de reaproveitar este except para todos os usos
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print('err', err)


def create_connection():
    try:
        cnx = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
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


def add_candidate(cnx, cursor, name: str, score: float, cpf: str):
    add_candidates = ("INSERT INTO candidates "
                      "(name, score, cpf) "
                      "VALUES (%s, %s, %s)")

    data_candidates = (name, score, cpf)

    cursor.execute(add_candidates, data_candidates)
    cnx.commit()

    return 'Ok - inserted'


def db_init():
    try:
        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1"
        )
        cursor = mydb.cursor()

        cursor.execute("DROP DATABASE IF EXISTS sample_university")
        cursor.execute("CREATE DATABASE sample_university")
        cursor.close()

        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
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
