from app import db_init
from db import add_candidate

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://sample-university-site.herokuapp.com',
    ]

    # Drop and create database
    db_init()

    def parse_candidate(self, response):
        [name, score] = response.xpath('//div/text()').getall()

        add_candidate(name, score)

    def parse(self, response):
        for candidate_href in response.css('li a::attr(href)').extract():
            yield response.follow(candidate_href, self.parse_candidate)

        next_page = response.css('div a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
