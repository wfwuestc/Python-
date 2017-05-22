from bs4 import BeautifulSoup
import urllib

url = 'C://Users/wfw/Documents/python_study/webcrawler/Plan-for-combating-master/week1/1_2/1_2answer_of_homework' \
      '/1_2_homework_required/index.html '
with open(url, 'r') as html:
    bs_obj = BeautifulSoup(html.read(), 'lxml')
    images = bs_obj.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = bs_obj.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = bs_obj.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars = bs_obj.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    reviews = bs_obj.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    print(stars)

for images, titles, prices, stars, reviews in zip(images, titles, prices, stars, reviews):
    data = {
        'title': titles.get_text(),
        'images': images.get('src'),
        'prices': prices.get_text(),
        'reviews': reviews.get_text(),
        'stars': len(stars.find_all('span', "glyphicon glyphicon-star"))
    }
    print(data)
