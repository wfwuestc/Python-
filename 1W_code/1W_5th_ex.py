'''
    动态网页异步加载例程
'''
from bs4 import BeautifulSoup
import requests
import time

header = {
            "User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
url = 'https://knewone.com/discover?page='

def get_page(url,data=None):

    web_data = requests.get(url,header)
    soup = BeautifulSoup(web_data.text,'lxml')
    imgs = soup.select('article > header > a > img')
    titles = soup.select('article > section > h4 > a')
    links = soup.select('article > section > h4 > a')

    if data == None:
        for img,title,link in zip(imgs,titles,links):
            data = {
                'img':img.get('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)

def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

get_more_pages(1,5)