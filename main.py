import requests
import os
import time
from bs4 import BeautifulSoup


def get_images(url, next=False):
    ts = time.time()  # start timer
    _, _, _, _, title, chapter, _ = url.split('/')  # get directory names
    try:
        os.makedirs(f'{title}/{chapter}')  # create folders
    except:
        print("Folder already exist.")

    # get images links
    html_doc = requests.get(url=url, headers=header).content
    print(f'Accessed url: {url}')
    soup = BeautifulSoup(html_doc, 'html.parser')
    reading_content = soup.find_all('div', class_="reading-content")[0]
    next_url = soup.find('a', class_="next_page").get('href')
    images = reading_content.find_all('img')
    images_links = [i.get('src').strip() for i in images]
    img_count = len(images_links)
    print(f"{img_count} image links retrieved.")

    # download images
    if chapter.find('raw') == -1:
        for idx, link in enumerate(images_links):
            print(f"Downloading image [{idx + 1} / {img_count}]...")
            img = requests.get(link, headers=header).content
            with open(f'{title}/{chapter}/{idx+1}.jpg', 'wb') as file:
                file.write(img)
    else:
        print("RAW chapter found. Skipping...")
    if next and next_url:
        get_images(next_url, True)
    else:
        print(
            f"All images downloaded succesfully ({(time.time() - ts).__floor__()}s). Program is exiting.")


endpoint = "https://mangaforfree.net/manga"
title = "touch-to-unlock-32"
chapter = "chapter-84-eng"
url = f"{endpoint}/{title}/{chapter}/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

get_images(url, True)
