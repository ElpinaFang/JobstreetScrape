import scrapy
import csv
import json

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.jobstreet.co.id/id/analyst-jobs-in-information-communication-technology/in-Jakarta-Raya'
    ]
       
    def parse(self, response):
        items = response.css("article")
        jobs_csv = []
        jobs_json = []
        for x in items:
            jobtitle = x.css("a[data-automation='jobTitle']::text").extract()
            company = x.css("a[data-automation='jobCompany']::text").extract()
            location = x.css("a[data-automation='jobLocation']::text").extract()
            if jobtitle and company and location:
                jobs_csv.append([jobtitle[0], company[0], location[0]])
                jobs_json.append({
                    "jobtitle": jobtitle[0],
                    "company": company[0],
                    "location": location[0]
                })
        if jobs_csv:
            with open('items.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["jobtitle", "company", "location"])
                writer.writerows(jobs_csv)
        if jobs_json:
            json.dump(jobs_json, open('items.json', 'w'))
                
            
        