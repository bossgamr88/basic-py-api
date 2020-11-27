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

# search_input = driver.find_element_by_xpath('//input[@aria-label="Search"]')
# search_input.send_keys('digimon anime') # test
# search_input.send_keys(Keys.RETURN)

driver.get(url)

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

description = atag.text.strip()
url = 'https://www.amazon.com' + atag.get('href')

# Price  :  tag span class : a-price
price_parent = item.find('span', 'a-price')
print(price_parent)

#  a-offscreen = $105.00
price = price_parent.find('span' , 'a-offscreen').text
print(price)

#  rating star
rating = item.i.text
print(rating)

# review count  - tag span class : class="a-size-base" dir="auto"
review_count = item.find('span',{'class' :'a-size-base','dir' :'auto'}).text
print(review_count)

# Generalize the pattern
# def extract_record(item):
#     "Extract and return data from a single record "
#
#     # description and url
#     atag = item.h2.a
#     description = atag.text.strip()
#     url = 'https://www.amazon.com' + atag.get('href')
#
#     # price
#     price_parent = item.find('span', 'a-price')
#     price = price_parent.find('span', 'a-offscreen').text
#
#     # rank and rating
#     rating = item.i.text
#     review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
#
#     result = (description,price,rating,review_count,url)
#
#     return result
#
# # records list empty contain pattern
# records = []
# results = soup.find_all('div', {'data-component-type': 's-search-result'})
# for item in results:
#     records.append(extract_record(item))

# Error handling ('NoneType' object has no attribute 'find')
def extract_record(item):
    "Extract and return data from a single record "

    # description and url
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    try:
        # price
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    try:
        # rank and rating
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description,price,rating,review_count,url)

    return result

records = []
results = soup.find_all('div', {'data-component-type': 's-search-result'})
for item in results:
    record = extract_record(item)
    if record:
        records.append(record)

# Check data
# records[0]
# print(records[0])

for row in records:
    print(row[1])

# Web driver click - Getting the next page
# tick : query url - query parameter page number

def get_url(search_item):
    "Generate a url from search item"
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_item = search_item.replace(' ', '+')

    # add term query to url
    url = template.format(search_item)

    # add page query placeholdder
    url += '&page{}'

    return url

# Putting it all together
def main(seach_term):

    # start up the webdriver

    record = []
    url = get_url(seach_term)

    for page in range(1,10): # กำหนดจำนวน loop ดึงหน้า default คือ 21
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    return record

main('digimon anime')

driver.close()

# save data to csv file
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Description','Price','Rating','ReviewCount','Url'])
    writer.writerows(records) # writerow ไม่เติม s เเม่งจะเป็นเเนวนอนหมดเลย โครตซวย 55



















