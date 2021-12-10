# manga-scraper
Manga downloader for mangaforfree.net

## How to Use?

To download a manga of your choice, just replace the following in the main.py.

```python
endpoint = endpoint = "https://mangaforfree.net/manga" #the website
title = "touch-to-unlock-32" #the title of manga as indicated in the URL
chapter = "chapter-84-eng" #the chapter of manga as indicated in the URL
```

To automatically download next chapter, set this to True.
```python
get_images(url, True)
```
