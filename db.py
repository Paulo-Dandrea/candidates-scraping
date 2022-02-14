import json
import mysql.connector
from mysql.connector import errorcode


def get_candidates():
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

    return json.dumps(json_data)

def add_candidate(widget, description):
    try:
        cnx = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="sample_university"
        )
        cursor = cnx.cursor()

        add_candidates = ("INSERT INTO candidates "
                          "(name, description) "
                          "VALUES (%s, %s)")

        data_candidates = (widget, description)

        cursor.execute(add_candidates, data_candidates)

        cnx.commit()

        cursor.close()
        cnx.close()

        return 'Ok - inserted'

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print('err', err)

def db_init():
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
    cursor.execute(
        "CREATE TABLE candidates (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return 'init database'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
