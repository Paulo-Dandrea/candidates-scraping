# External libs
import scrapy
from validate_docbr import CPF
from operator import itemgetter
# helpers
from helpers.candidate_cleaner import Candidate
# database
from database.candidate.add import add_candidate
from database.connection.create_connection import create_connection



cpf = CPF()


class CandidatesSpider(scrapy.Spider):
    name = 'candidates'
    start_urls = [
        'https://sample-university-site.herokuapp.com',
    ]

    custom_settings = {
        'LOG_ENABLED': False,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CONCURRENT_REQUESTS': 32,
    }

    def __init__(self):
        self.cnx = create_connection()
        self.cursor = self.cnx.cursor()

    def parse_candidate(self, response):
        [name, score] = response.xpath('//div/text()').getall()

        cleaned_candidate = Candidate(
            name, score, response.url).get_cleaned_candidate()

        name, score, unverified_cpf = itemgetter(
            'name', 'score', 'cpf')(cleaned_candidate)

        if cpf.validate(unverified_cpf):
            print('isValid')
            add_candidate(self.cnx, self.cursor, name, score, unverified_cpf)

    def parse(self, response):
        for candidate_href in response.css('li a::attr(href)').extract():
            yield response.follow(candidate_href, self.parse_candidate)

        next_page = response.css('div a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            self.cursor.close()
            self.cnx.close()
