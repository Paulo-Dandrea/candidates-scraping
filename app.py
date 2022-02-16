
from db import db_init, get_candidates

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
    return get_candidates()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
