import requests
from bs4 import BeautifulSoup
from urllib import request
import time

url = 'http://weheartit.com/inspirations/taylorswift?page='

for i in range(21):
    i = str(i+1)
    url1 = url + i
    print(url1)
    data = requests.get(url1)
    soup = BeautifulSoup(data.text,'lxml')
    imgs = soup.select('div > div.no-padding > div > a > img')
    img_link = []
    for item in imgs:
        link = item.get('src')
        img_link.append(link)
    folder_path = 'C://Users/wfw/Documents/python_study/webcrawler/TAYLOR/'

    for link in img_link:
        print(link)
        request.urlretrieve(link , folder_path + link[-23:-17] + link[-4:])
        time.sleep(0.5)
    print('Done')

print('Done')