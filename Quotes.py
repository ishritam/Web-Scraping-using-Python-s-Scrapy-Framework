# -*- coding: utf-8 -*-
import scrapy

inp = int(input("Enter the no. of pages you want to scrap: "))
class ThescrapySpider(scrapy.Spider):
    name = 'Thescrapy'
    start_urls = ['http://quotes.toscrape.com/page/{}/'.format(n) for n in range(1,inp)]

    def parse(self, response):
        data = {}
        books = response.css('div.row')
        for book in books:
        	for b in book.css('div.quote'):
        		data['Quote'] = b.css('span::text').getall()[0]
        		data['Author'] = b.css('small.author::text').getall()
        		data['Tag'] = b.css('a.tag::text').getall()
        		data['About the Author'] = 'http://quotes.toscrape.com' + b.css('a::attr(href)').getall()[0]
        		yield data
