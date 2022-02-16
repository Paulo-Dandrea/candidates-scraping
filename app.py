
from database.connection.create_connection import create_connection
from database.candidate.get_all import get_all_candidates
from database.connection.init_db import db_init

from flask import Flask
from subprocess import call

app = Flask(__name__)


@app.route('/create-db')
def create_db():
    return db_init()


@app.route('/start-scraping')
def start_scraping():
    call(["scrapy", "runspider", "candidates_spider.py"])

    return 'Scrapy completed'


@app.route('/candidates')
def candidates():
    cnx = create_connection()
    cursor = cnx.cursor()

    return get_all_candidates(cursor)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
