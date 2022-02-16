from helpers import Candidate
import scrapy
from db import add_candidate, db_init
from operator import itemgetter


# Este spider provavelmente não deveria adicionar diretamente no banco de dados.
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

    # Drop and create database
    db_init()

    def parse_candidate(self, response):
        [name, score] = response.xpath('//div/text()').getall()

        cleaned_candidate = Candidate(name, score, response.url).get_cleaned_candidate()

        name, score, cpf = itemgetter(
            'name', 'score', 'cpf')(cleaned_candidate)

        add_candidate(name, score, cpf)

        yield {
            'name': name,
            'score': score,
            'cpf': cpf,
        }

    def parse(self, response):
        for candidate_href in response.css('li a::attr(href)').extract():
            yield response.follow(candidate_href, self.parse_candidate)

        next_page = response.css('div a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
