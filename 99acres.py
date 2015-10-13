from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup,SoupStrainer
import csv

browser = webdriver.Firefox()
'''
browser.get("http://www.99acres.com/property/loginpage.php")

elem = browser.find_element_by_name("username")
elem.send_keys("ks485@snu.edu.in")
elem = browser.find_element_by_name("password")
elem.send_keys("k123456")
login=browser.find_element_by_class_name("srchprobtn").submit()
elem=browser.find_element_by_id("HmMenuTTPID")
elem.send_keys(Keys.RETURN)
'''
browser.get("http://www.99acres.com/property-in-greater-noida-ffid")
hidden_submenu = browser.find_element_by_id("HmMenuTTPID")
ActionChains(browser).move_to_element(hidden_submenu).click(hidden_submenu).perform()
time.sleep(2)
elemclick=browser.find_element_by_id("loginHeader")
ActionChains(browser).move_to_element(elemclick).click(elemclick).perform()
time.sleep(3)
elem = browser.find_element_by_name("username")
elem.send_keys("ks485@snu.edu.in")
elem = browser.find_element_by_name("password")
elem.send_keys("k123456")
login=browser.find_element_by_id("submit_query1").submit()
time.sleep(2)
phonenum=browser.find_element_by_link_text("View Phone Number").click()
time.sleep(2)
buyerclick=browser.find_element_by_name("individualRadio").click()
time.sleep(1)
submitbutton=browser.find_element_by_name("name").submit()
time.sleep(10)
viewphonearr=browser.find_elements_by_link_text("View Phone Number")

list_name=[]
list_mobile=[]
'''
html = browser.page_source
relData = SoupStrainer('div',{'id': 'lgndiv'})
html=open('n.html').read()
soup=BeautifulSoup(html,"lxml",parse_only=relData)
print(soup.find_all('td'))
name=soup.findAll('td')[1].text.strip("\n").strip(' ').strip("\n")
mobile=soup.findAll('td')[3].text.strip("\n").strip(' ').strip("\n")
a={}
a[name]=mobile
print(name)
print(mobile)
'''
count=len(viewphonearr)
for i in viewphonearr:
    print('waiting 5 seconds')
    time.sleep(5)
    i.send_keys(Keys.RETURN)
    print('waiting 5seconds')
    time.sleep(5)
    print(count)
    count=count-1


html = browser.page_source
relData = SoupStrainer('div',{'id': 'lgndiv'})
soup=BeautifulSoup(html,"lxml",parse_only=relData)
#print(soup.prettify())
result={}
list_name=[]
list_mobile=[]
name=''
phone=''
#print(soup.findAll('td'))
for tag in soup.findAll('td'):
    if tag.text.strip("\n").strip(' ').strip("\n")== 'Name :':
        name=tag.find_next_sibling().text.strip("\n").strip(' ').strip("\n")
        list_name.append(name)
    if tag.text.strip("\n").strip(' ').strip("\n")== 'Mobile :':
        phone=tag.find_next_sibling().text.strip("\n").strip(' ').strip("\n")
        list_mobile.append(phone)
    result[name]=phone


writer = csv.writer(open('visual.csv', 'a'))
for key, value in result.items():
    writer.writerow([key, value])
