# -*- coding: utf-8 -*-
import scrapy

#=================================books scrapiing=====================================
dic = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}

inp = int(input("Enter the no. of pages you want to scrap: "))
class ThescrapySpider(scrapy.Spider):
    name = 'Thescrapy'
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(n) for n in range(1,inp)]

    def parse(self, response):
        data = {}
        books = response.css('ol.row')
        for book in books:
        	for b in book.css('article.product_pod'):
        		data['Title'] = b.css('a::attr(title)').getall()
        		data['Price'] = b.css('div.product_price p.price_color::text').getall()[0].split()[0]
        		data['Stock'] = b.css('div.product_price p.instock.availability::text').getall()[1].strip()  #you can give space instock availability
        		data['Star'] = b.css('p::attr(class)').getall()[0].split()[-1]
        		data['Star'] = [j for i,j in dic.items() if i in data['Star']][0]

        		yield data