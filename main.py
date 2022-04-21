import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os


CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
GOOGLE_FORM_LINK = os.getenv("GOOGLE_FORM_LINK")
OTODOM_LINK = os.getenv("OTODOM_LINK")

website = requests.get(OTODOM_LINK)
soup = BeautifulSoup(website.text, 'html.parser')

links = []
for link_element in soup.find_all(name="a", class_="css-rvjxyq es62z2j14"):
    link = link_element.get("href")
    prefix = "https://www.otodom.pl"
    if prefix not in link:
        link = f"{prefix}{link}"
    links.append(link)

price_elements = [price_element.text for price_element in soup.find_all(name="span", class_="css-rmqm02 eclomwz0")]
price_elements_list = price_elements[::4]
prices = [price_element.replace(u'\xa0', u' ') for price_element in price_elements_list]

addresses = [address.text for address in soup.find_all(name="span", class_="css-17o293g es62z2j9")]

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

for n in range(len(links)):
    driver.get(GOOGLE_FORM_LINK)

    time.sleep(2)

    property_address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(addresses[n])

    property_price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price.send_keys(prices[n])

    property_link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(links[n])

    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
