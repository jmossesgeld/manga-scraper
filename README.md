# manga-scraper
Manga downloader for mangaforfree.net

## How to Use?

### Install Python
https://www.python.org/downloads/

### Install dependencies
- open the terminal.
- cd into the repo directory
- run `pip install requirements.txt`

To download a manga of your choice, just replace the following in the main.py.

```python
mangaforfree("https://mangaforfree.net/manga/{TITLE}/{CHAPTER}/", True)
```
It is advisable to copy the link directly from the website to avoid typos.
To automatically download next chapters, set download_next argument to True.
