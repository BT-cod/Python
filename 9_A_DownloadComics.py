
import requests
import os
from bs4 import BeautifulSoup
url = "https://xkcd.com/1/"
if not os.path.exists("xkcd_comics"):
    os.makedirs("xkcd_comics")
while True:
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    comic_elem = soup.select_one("#comic img")
    if comic_elem:
        comic_url = "https:" + comic_elem["src"]
        print(f"Downloading {comic_url}....")
        res = res = requests.get(comic_url)
        res.raise_for_status()
        image_file_path = os.path.join("xkcd_comics", os.path.basename(comic_url))
        with open(image_file_path, "wb") as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
    prev_link = soup.select_one("a[rel='prev']")
    if not prev_link:
        break
    url = "https://xkcd.com/" + prev_link["href"]
print("All comics downloaded..")