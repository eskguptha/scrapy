# scrapy runspider giordano.py -o 1.json
# scrapy runspider giordano.py -o 1.csv
import scrapy
from scrapy.http import Request
class RevenueMantraCrawler(scrapy.Spider):
    name = 'crawler'
    start_urls = ['http://www.domain.com/page/1','http://www.domain.com/page/2']
    def parse(self, response):
        for content in response.xpath('//div[@class="articleList"]'):
            
            yield {
                'title': content.xpath('//div[@class="articleImage"]/a/@title').extract_first(),
                'description': content.xpath('//div[@class="articleDetails"]//div[@class="intro"]/text').extract_first().strip(),
                'image_url': content.xpath('//div[@class="articleImage"]/a/img/@src').extract_first(),
                'link': response.urljoin(content.xpath('//div[@class="articleImage"]/a/@href').extract_first())
            }
        url = response.urljoin(response.xpath('//div[@class="paging"]//div[@class="next"]/a/@href').extract_first())
        yield scrapy.Request(url, callback=self.parse)
