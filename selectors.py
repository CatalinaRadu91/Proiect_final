import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.get('https://www.zonia.ro/')
time.sleep(5)
cookies = chrome.find_element(By.LINK_TEXT, "Permite")
cookies.click()
contulmeu = chrome.find_element(By.LINK_TEXT, "Contul meu")
contulmeu.click
time.sleep(5)