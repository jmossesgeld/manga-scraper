import requests
import os
from bs4 import BeautifulSoup
from bs4.element import Tag, ResultSet
from typing import Iterable, cast

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}


def mangaforfree(url):
    # get title and chapter from url
    _, _, _, _, title, chapter, _ = url.split('/')

    # request html
    html_doc = requests.get(url=url, headers=header).content
    print(f'Accessed url: {url}')

    # create soup
    soup = BeautifulSoup(html_doc, 'html.parser')
    reading_content: Tag = soup.find_all(
        'div', class_="reading-content")[0]

    # get link of next chapter
    try:
        next_url = soup.find('a', class_="next_page").get('href')
    except:
        next_url = False

    # get link of images
    images: ResultSet = reading_content.find_all('img')
    images_links = [i.get('src').strip()
                    for i in cast(Iterable[Tag], images)]
    img_count = len(images_links)
    print(f"{img_count} image links retrieved.")

    if chapter.find('raw') == -1:
        # create folders
        try:
            os.makedirs(f'downloaded/{title}/{chapter}')
        except:
            print("Folder already exist.")
        # download images
        for idx, link in enumerate(images_links):
            print(f"Downloading image [{idx + 1} / {img_count}]...")
            img = requests.get(link, headers=header).content
            with open(f'downloaded/{title}/{chapter}/{idx+1}.jpg', 'wb') as file:
                file.write(img)
    else:
        print("RAW chapter found. Skipping...")
    if next and next_url:
        # download next chapter by recursing this function
        mangaforfree(next_url, True)
    else:
        print(
            f"All images downloaded succesfully. Program is exiting.")


mangaforfree("https://mangaforfree.net/manga/touch-to-unlock-45/chapter-1/")
