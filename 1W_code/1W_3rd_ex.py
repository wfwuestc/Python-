
from bs4 import BeautifulSoup
import urllib

url ='file:///C:/Users/wfw/Documents/python_study/webcrawler/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html#'
with open(url) as html:
	bs_obj = BeautifulSoup(html)
	print(bs_obj.text)