from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# instantiate webdriver
web_driver = webdriver.Chrome()

# get page
web_driver.get("http://www.google.com")

# search page
search_box = web_driver.find_element_by_xpath('//input[contains(@title, "Search")]')
search_box.send_keys("happy returns")

# submit search (note: path to button is not unique, leveraging keyboard enter)
search_box.submit()

# Sorry cannot finish in time
