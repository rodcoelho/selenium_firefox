#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

websites = ['https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-25;r=2018-03-31',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-18;r=2018-03-31',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-11;r=2018-03-31',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-04;r=2018-03-31',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-25;r=2018-03-31',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-18;r=2018-03-25',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-11;r=2018-03-18',
            'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;d=2018-03-04;r=2018-03-11']

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def lookup(driver):

    # loads page
    for sites in websites:
        time.sleep(3)
        driver.get(sites)

        timeout = 20
        try:
            WebDriverWait(driver, timeout)
            driver.implicitly_wait(10)
            # get text within div class
            element = driver.find_element_by_class_name('LJV2HGB-d-Ab')

            print(element.get_attribute('innerHTML'))

        except TimeoutException:
            print("Error")
            driver.quit()





if __name__ == "__main__":
    # init driver
    driver = init_driver()
    # tell driver to look up query on google
    lookup(driver)

    # close driver
    driver.quit()
