import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# ref : https://www.youtube.com/watch?v=3KaffTIZ5II

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

# know xpath : https://www.w3schools.com/xml/xpath_intro.asp
username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('pakawat.work88@gmail.com')

my_password = getpass('enter password: ')

password = driver.find_element_by_xpath('//input[@name="session[password]"]')
password.send_keys(my_password)

password.send_keys(Keys.RETURN)

# aria-label="Search query"
search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('#tokyo')
search_input.send_keys(Keys.RETURN)

driver.find_element_by_link_text('Latest').click()

# tag div : data-testid="tweet"
# cards = driver.find_element_by_xpath('//div[@data-testid="tweet"]')
# cards = cards[0]