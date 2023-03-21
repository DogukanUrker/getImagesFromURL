import requests
from bs4 import BeautifulSoup

url = "https://www.ekleristan.com/urunler/"
page = requests.get(url).text
soup = BeautifulSoup(page)
images = soup.findAll("img")


def toTXT(url, fileName="images"):
    f = open(fileName + ".txt", "a")
    for image in images:
        f.write(image["src"] + "\n")
    f.close()


def toFolder(url, folderName="images", fileFormat="raw"):
    pass
