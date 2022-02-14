
# Mind use of anaconda. Now, pip is using anaconda and vscode as well.
# Before, vscode was not using anaconda.
import mysql.connector
import json
from flask import Flask
from mysql.connector import errorcode

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM widgets")

    # this will extract row headers
    row_headers = [x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps(json_data)


# @app.route('/add_something')
def add_something(widget, description):
    try:
        cnx = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="inventory"
        )
        cursor = cnx.cursor()

        add_widgets = ("INSERT INTO widgets "
                       "(name, description) "
                       "VALUES (%s, %s)")

        data_widgets = (widget, description)

        cursor.execute(add_widgets, data_widgets)

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


# @app.route('/initdb')
def db_init():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute(
        "CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return 'init database'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
