import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Setup
driver = webdriver.Chrome()
url = 'https://www.amazon.com/'
driver.get(url)

def get_url(search_item):
    "Generate a url from search item"
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_item = search_item.replace(' ', '+')
    return template.format(search_item)

url = get_url('digimon anime')
print(url)

search_input = driver.find_element_by_xpath('//input[@aria-label="Search"]')
search_input.send_keys('digimon anime') # test
search_input.send_keys(Keys.RETURN)

# Extract the collection
soup = BeautifulSoup(driver.page_source, 'html.parser')

# tag span class : class="celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results"
# tag div class : class="sg-col-inner"
# tag span  key : data-component-type="s-search-results" , class="rush-component s-latency-cf-section"

# s-search-result = index list
# s-search-results = all index

results = soup.find_all('div', {'data-component-type': 's-search-result'})
len(results)
print(len(results)) # item list

# Prototype the record
item = results[0]

# title tag h2
atag = item.h2.a
# atag.text
# print(atag.text)



