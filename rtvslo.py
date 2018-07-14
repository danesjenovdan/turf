import requests, scrapy

class RtvSloSpider(scrapy.Spider):
  name = 'RTVSlospider'
  start_urls = ['http://www.rtvslo.si/slovenija/']
  total_comments = 0

  def get_comments(self, response):
    # get all comments on page
    print('I have parsed ' + str(self.total_comments) + ' comments.')

    number_of_comments = len(response.css('.com'))
    article_id = response.meta['article_id']
    current_page = response.meta['page']
    href = response.meta['href']

    self.total_comments += number_of_comments
    for comment in response.css('.com'):

      yield {
        'username': comment.css('.ac a::text')[0].extract().strip(),
        'timestamp': comment.css('.ac ::text').extract()[-1].strip(),
        'text': ' '.join([text.strip() for text in comment.css('.ds2').css('::text').extract()]),
        'upvotes': ' '.join([text.strip() for text in comment.css('.tcu').css('::text').extract()]).strip(),
        'downvotes': ' '.join([text.strip() for text in comment.css('.tcd').css('::text').extract()]).strip(),
        'article_id': article_id,
        'page': current_page,
        'href': href
      }
    
    if number_of_comments > 0:
      comments_link = 'http://www.rtvslo.si/index.php?&c_mod=news&op=comments&func=ajax&page=' + str(current_page + 1) + '&hash=0&sort=asc&id=' + str(article_id)
      yield scrapy.Request(url=comments_link, callback=self.get_comments, meta={'article_id': article_id, 'page': current_page + 1, 'href': href})

  def parse(self, response):
    for link in response.css('a.title'):
      article_id = link.css('::attr(href)').extract_first().split('/')[-1]
      href = link.css('::attr(href)').extract_first()

      comments_link = 'http://www.rtvslo.si/index.php?&c_mod=news&op=comments&func=ajax&page=0&hash=0&sort=asc&id=' + str(article_id)

      print('Started parsing comments at ' + href)
      yield scrapy.Request(url=comments_link, callback=self.get_comments, meta={'article_id': article_id, 'page': 0, 'href': href})