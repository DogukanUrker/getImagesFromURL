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
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found")
    f = open(fileName + ".txt", "a")
    for image in getImages(url):
        f.write(image + "\n")
    f.close()
    print(f"\n\033[92m{len(getImages(url))}\033[0m images saved to {fileName}.txt")


def toFolder(url, folderName="images", imageFormat="png"):
    match exists(folderName):
        case False:
            mkdir(folderName)
    imageCount = 1
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found\n")
    for image in getImages(url):
        r = requests.get(image, stream=True)
        r.raw.decode_content = True
        imageName = Path(r.url).stem
        with open(f"{folderName}/{imageName}.{imageFormat}", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        print(f"Image: \033[93m{imageCount}\033[0m downloaded")
        imageCount += 1
    print(f"\n\033[92m{len(getImages(url))}\033[0m images downloaded to /{folderName}")


toTXT(url)
toFolder(url)
