#漫画サイトのスクレイピング
from bs4 import BeautifulSoup
import urllib.request
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

DRIVER_PATH = '{{/usr/local/bin/chromedriver}}'

driver = webdriver.Chrome(executable_path = DRIVER_PATH, chrome_options = options)

#webページアクセス
url = 'https://books.rakuten.co.jp/calendar/001001/weekly/?tid=2020-05-18'
driver.get(url)

html = driver.page_source
soup = beautifulsoup(html,"html.parser")

bk_title = [i.get_text() for i in  soup.select("[class='item-title__text']")]
date = [i.get_text() for i in soup.select("[class='item-release__date']")]
link = [tag.get('href') for tag in soup.select("[class='item-title'] a")]

title_list = []
date_list =[]
link_list =[]
print(len(bk_title))
print(len(date))
print(len(link))


#for i in range(len(bk_title)):
#    title_list.append([bk_title[i].text])
#    date_list.append([date[i].text.strip()])
#    link_list.append([link[i]])
#
#
#
#f = open("output.csv","w")
#date_f = open("output_date.csv","w")
#link_f = open("output_link.csv","w")
#writecsv = csv.writer(f,lineterminator='\n')
#write_date_csv = csv.writer(date_f,lineterminator='\n')
#write_link_csv = csv.writer(link_f,lineterminator='\n')
#
#writecsv.writerows(title_list)
#write_date_csv.writerows(date_list)
#write_link_csv.writerows(link_list)

f.close()
#page_li = soup.select("[class='rbcomp__pager'] li")
#print(page_li)
## page_len = [sub.select('a') for sub in soup.select("[class='rbcomp__page'] li")]
#
#
#print(len(page_li))
#
##while(page_flag)
#bk_title = soup.select("[class='item-title__text']")
#date = soup.select("[class='item-release__date']")
#link = [tag.get('href') for tag in soup.select("[class='item-title'] a")]
#
#title_list = []
#date_list =[]
#link_list =[]
#print(len(bk_title))
#print(len(date))
#print(len(link))
#
#
#for i in range(len(bk_title)):
#    title_list.append([bk_title[i].text])
#    date_list.append([date[i].text.strip()])
#    link_list.append([link[i]])
#
#
#
#f = open("output.csv","w")
#date_f = open("output_date.csv","w")
#link_f = open("output_link.csv","w")
#writecsv = csv.writer(f,lineterminator='\n')
#write_date_csv = csv.writer(date_f,lineterminator='\n')
#write_link_csv = csv.writer(link_f,lineterminator='\n')
#
#writecsv.writerows(title_list)
#write_date_csv.writerows(date_list)
#write_link_csv.writerows(link_list)
#
#f.close()
