from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome()
# url = 'https://www.google.com'
url = 'https://twitter.com/hashtag/tokyo'

driver.get(url)
page_html = driver.page_source

# print(type(page_html))

data = soup(page_html, 'html.parser')

# Basic selenium
# elem_search = driver.find_element_by_name("q")
# elem_search.clear()
# elem_search.send_keys("ลุงตู่")
# elem_search.send_keys(Keys.ENTER)

# twitter scraping basic
# tag div  class : css-1dbjc4n

tweettext = data.findAll('div',{'class':'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'})

print(tweettext)
print(type(tweettext)) # soup

for i,tw in enumerate(tweettext):
    print(i)
    print(tw.text)
