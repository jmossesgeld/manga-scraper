import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver


def get_images_data_src(endpoint, title, chapter):
    try:
        os.makedirs(chapter)
    except:
        print("Folder already exist.")
    url = f"{endpoint}/{title}/{chapter}/"

    html_doc = requests.get(
        url=url, headers=header).content
    soup = BeautifulSoup(html_doc, 'html.parser')

    reading_content = soup.find_all('div', class_="reading-content")[0]
    images = reading_content.find_all('img')
    images_links = [i.get('data-src').strip() for i in images]
    return images_links


endpoint = "https://toonily.com/webtoon"
title = "touch-unlock-0001"
chapter = "chapter-92"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

images_data_src = get_images_data_src(endpoint, title, chapter)

def get_images(links):
    chrome_driver_path = 'C:/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(links[0])
    driver.maximize_window()

get_images(images_data_src)


