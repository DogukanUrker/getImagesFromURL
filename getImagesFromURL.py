import requests
from bs4 import BeautifulSoup
import shutil
from os.path import exists
from os import mkdir
from pathlib import Path

url = "https://www.ekleristan.com/urunler/"

import sys


def getImages(url):
    images = []
    page = requests.get(url).text
    soup = BeautifulSoup(page)
    imageLinks = soup.findAll("img")
    for image in imageLinks:
        images.append(image["src"]),
    return images


def toTXT(url, fileName="images"):
    f = open(fileName + ".txt", "a")
    for image in getImages(url):
        f.write(image + "\n")
    f.close()


def progressbar(it, prefix="", size=60, out=sys.stdout):  # Python3.3+
    count = len(it)

    def show(j):
        x = int(size * j / count)
        print(
            "{}[{}{}] {}/{}".format(prefix, "#" * x, "." * (size - x), j, count),
            end="\r",
            file=out,
            flush=True,
        )

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)


def toFolder(url, folderName="images", imageFormat="png"):
    match exists(folderName):
        case False:
            mkdir(folderName)
    imageCount = len(getImages(url))
    print(f"{imageCount} images found")
    for image in getImages(url):
        r = requests.get(image, stream=True)
        r.raw.decode_content = True
        imageName = Path(r.url).stem
        with open(f"{folderName}/{imageName}.{imageFormat}", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
