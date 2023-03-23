import requests
from bs4 import BeautifulSoup
import shutil
from os.path import exists
from os import mkdir
from pathlib import Path


def getImages(url):
    images = []
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    imageLinks = soup.findAll("img")
    for image in imageLinks:
        images.append(requests.compat.urljoin(url, image.get("src"))),
    return images


def toTXT(url, fileName="images"):
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found")
    f = open(fileName + ".txt", "a")
    for image in getImages(url):
        f.write(image + "\n")
    f.close()
    print(f"\n\033[92m{len(getImages(url))}\033[0m images saved to {fileName}.txt")


def toFolder(url, folderName="images"):
    match exists(folderName):
        case False:
            mkdir(folderName)
    imageCount = 1
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found\n")
    for image in getImages(url):
        r = requests.get(image, stream=True)
        r.raw.decode_content = True
        imageName = Path(r.url).name.replace("?", "")
        with open(f"{folderName}/{imageName}", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        print(f"Image: \033[93m{imageCount}\033[0m saved")
        imageCount += 1
    print(f"\n\033[92m{len(getImages(url))}\033[0m images saved to /{folderName}")
