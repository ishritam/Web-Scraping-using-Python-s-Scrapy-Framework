# -*- coding: utf-8 -*-
import scrapy
inp = int(input("Enter the no. of pages you want to scrap: "))
class ThescrapySpider(scrapy.Spider):
    name = 'Thescrapy'
    start_urls = ['https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_0_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_0_0_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=mobiles&requestId=3a350485-fe86-4053-8ef7-7c17fcb673e3&page={}'.format(n) for n in range(1,inp)]

    def parse(self, response):
        data = {}
        books = response.css('div._1HmYoV._35HD7C')
        for book in books:
        	for b in book.css('a._31qSD5'):
        		data['Product'] = b.css('div._3wU53n::text').getall() 
        		data['Price'] = b.css('div._1vC4OE._2rQ-NK::text').getall() 
        		data['Off on Exchange'] = b.css('div._3_G5Wj::text').getall()
        		data['Off on Exchange'] = [data['Off on Exchange'][-2] if len(data['Off on Exchange'])==4 else data['Off on Exchange'][-1] if len(data['Off on Exchange'])==1 else 0]  
        		data['Star'] = b.css('div.hGSR34::text').getall()
        		yield data

        		
