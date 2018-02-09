#!/usr/bin/env python3
import time, requests, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from writeout import write_out_to_log

url_ip_location = 'http://ipinfo.io/json'
r = requests.get(url_ip_location).json()
r = r['city']

website = 'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=LHR;'
dates = [
        ['d=2018-03-25;r=2018-03-31', 'f1'],
        ['d=2018-03-18;r=2018-03-31', 'f2'],
        ['d=2018-03-11;r=2018-03-31', 'f3'],
        ['d=2018-03-04;r=2018-03-31', 'f4'],
        ['d=2018-03-25;r=2018-03-31', 'f5'],
        ['d=2018-03-18;r=2018-03-25', 'f6'],
        ['d=2018-03-11;r=2018-03-18', 'f7'],
        ['d=2018-03-04;r=2018-03-11', 'f8']
         ]
payload = {}

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def lookup(driver):

    # loads page
    for date in dates:
        time.sleep(random.uniform(1,6))
        driver.get(website+date[0])

        timeout = 20
        try:
            WebDriverWait(driver, timeout)
            driver.implicitly_wait(10)
            # get text within div class
            element = driver.find_element_by_class_name('LJV2HGB-d-Ab')
            price = (element.get_attribute('innerHTML'))
            # price = price[1:]
            payload[date[1]] = [price, r, date[1]]
        except TimeoutException:
            print("Error")
            driver.quit()

if __name__ == "__main__":
    # init driver
    driver = init_driver()
    # tell driver to look up query on google
    lookup(driver)
    write_out_to_log(payload, region=r)

    # close driver
    driver.quit()
