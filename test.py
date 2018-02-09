from pyvirtualdisplay import Display
from selenium import webdriver


display = Display(visible=0, size=(1920, 1080)).start()
browser = webdriver.Firefox()
browser.get("https://groups.google.com/forum/?hl=en#!forum/shiny-discuss")
print(browser.title.encode('utf8', 'replace'))
