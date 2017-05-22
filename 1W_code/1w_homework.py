import requests
from bs4 import BeautifulSoup

import re

url = 'http://bj.58.com/pbdn/1/'
header = {
    "User-Agent": 'Baiduspider-image',
    'Connection': 'close'
}

proxies = {'http': 'socks5://127.0.0.1:1080',
           'https': 'socks5://127.0.0.1:1080'}
'''
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
'''
print(url)
data = requests.get(url, header)
soup = BeautifulSoup(data.text, "html5lib")


links = soup.select('div#infolist > table.tbimg > tbody > tr > td.t > a.t')

link = []

for item in links:
    link.append(item.get('href').split('?')[0])
print(link)
for url1 in link:
    data1 = requests.get(url1, header)
    soup1 = BeautifulSoup(data1.text, 'lxml')

    zone = soup1.select('.crb_i > a')[0].text


    title = soup1.select('.mainTitle > h1')[0].text


    date = soup1.select('.time')[0].text


    price = soup1.select('.price')[0].text


    chense = soup1.select('.suUl > li > div.su_con > span')
    chense = str(chense[1])
    chense = re.findall(r'\s+(.*?)\s+', chense)[0]

    ak = str(soup1)
    name = re.findall(r'linkman:\'(.*?)\',', ak)[0]

    hub = {
        'title': title,
        'zone': zone,
        'date': date,
        'price': price,
        'chense': chense,
        'name': name
    }
    print(hub)
