#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    # loads page
    driver.get("http://www.google.com")
    try:
        # waits for query box element to be located
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        # waits for the search button to be click-able
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        # places query into the search box
        box.send_keys(query)
        # clicks the button
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    # init driver
    driver = init_driver()
    # tell driver to look up query on google
    lookup(driver, "Selenium")
    time.sleep(5)
    # close driver
    driver.quit()