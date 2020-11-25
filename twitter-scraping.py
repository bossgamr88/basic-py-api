from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://www.google.com'

driver.get(url)

# Basic selenium
elem_search = driver.find_element_by_name("q")
elem_search.clear()
elem_search.send_keys("ลุงตู่")
elem_search.send_keys(Keys.ENTER)

