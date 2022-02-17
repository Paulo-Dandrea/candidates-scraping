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

    # Settings for better performance of the spider
    custom_settings = {
        'LOG_ENABLED': False,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CONCURRENT_REQUESTS': 32,
    }

    # Connect to the database
    def __init__(self):
        self.cnx = create_connection()
        self.cursor = self.cnx.cursor()

    # 2. Parsing the candidate page
    def parse_candidate(self, response):
        # First <div> holds the name
        # Second <div> holds the score
        [name, score] = response.xpath('//div/text()').getall()

        # Get hygienized candidate data
        cleaned_candidate = Candidate(
            name, score, response.url).get_cleaned_candidate()
        name, score, unverified_cpf = itemgetter(
            'name', 'score', 'cpf')(cleaned_candidate)

        # Only if the CPF is valid, add the candidate to the database
        if cpf.validate(unverified_cpf):
            # Send the connection and the cursor to it
            add_candidate(self.cnx, self.cursor, name, score, unverified_cpf)

    # 1. Parsing the approved candidates page
    def parse(self, response):
        # For each candidate of the list, follow the candidate page
        for candidate_href in response.css('li a::attr(href)').extract():
            yield response.follow(candidate_href, self.parse_candidate)

        # Get the next page button, with there is a next,
        # follow it recursively with this very same method
        next_page = response.css('div a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # When the spider finishes, close the connection
        else:
            self.cursor.close()
            self.cnx.close()
