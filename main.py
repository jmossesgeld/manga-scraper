import requests
import os
from bs4 import BeautifulSoup


def get_images(endpoint, title, chapter):
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
    images_links = [i.get('src').strip() for i in images]
    img_count = len(images_links)
    print(f"{img_count} image links retrieved.")
    for idx, link in enumerate(images_links):
        print(f"Downloading image [{idx + 1} / {img_count}]...")
        img = requests.get(link, headers=header).content
        with open(f'{chapter}/{idx}.jpg', 'wb') as file:
            file.write(img)
            print(f"Image saved succesfully.")
    print("All images downloaded succesfully")



endpoint = "https://mangaforfree.net/manga"
title = "touch-to-unlock-30"
chapter = "chapter-96-eng"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

get_images(endpoint, title, chapter)

