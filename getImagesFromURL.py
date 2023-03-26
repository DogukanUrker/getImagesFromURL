import shutil
import requests
from os import mkdir
from pathlib import Path
from os.path import exists
from bs4 import BeautifulSoup


def getImages(url):
    images = []
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    imageLinks = soup.findAll("img")
    for image in imageLinks:
        images.append(requests.compat.urljoin(url, image.get("src")[:350])),
    return images


def toFile(url, fileName="images"):
    if not ".txt" in fileName:
        fileName += ".txt"
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found 🔎")
    f = open(fileName, "a")
    for image in getImages(url):
        f.write(image + "\n")
    f.close()
    print(f"\n\033[92m{len(getImages(url))}\033[0m images saved to {fileName} 💾")


def toFolder(url, folderName="images"):
    match exists(folderName):
        case False:
            mkdir(folderName)
    imageCount = 1
    print(f"\n\033[94m{len(getImages(url))}\033[0m images found 🔎\n")
    for image in getImages(url):
        r = requests.get(image, stream=True)
        r.raw.decode_content = True
        imageName = Path(r.url).name.replace("?", "")
        if not "." in imageName:
            imageName += ".png"
        with open(f"{folderName}/{imageName}", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        print(
            f'Image \033[95m{imageCount}\033[0m: "\033[93m{imageName}\033[0m" saved from "\033[94m{image}\033[0m"\n'
        )
        imageCount += 1
    print(f"\n\033[92m{len(getImages(url))}\033[0m images saved to /{folderName} 💾")
