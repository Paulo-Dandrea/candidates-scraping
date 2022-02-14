from app import add_something, db_init
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://sample-university-site.herokuapp.com',
    ]

    db_init()

    # add_something('name', 'score')

    # Como passar como argumento o CPF

    def parse_candidate(self, response):
        [name, score] = response.xpath('//div/text()').getall()
        add_something(name, score)

        yield {
            'nome': name,
            'score': score,
        }

    def parse(self, response):
        for candidate_href in response.css('li a::attr(href)').extract():
            yield response.follow(candidate_href, self.parse_candidate)

        next_page = response.css('div a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
