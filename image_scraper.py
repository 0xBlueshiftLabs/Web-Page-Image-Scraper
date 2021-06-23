from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re


# url to be scraped
parent_url = ""

#destination folder for scraped images
file_path = ""


# finds all the image URLs from the HTML and stores them in a list
html = urlopen(parent_url)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
urls = []
for image in images:
    urls.append(image['src'])

# replaces parts of the url to get hi res images (only applicable for this website instance)
counter = 0
for url in urls:
    a = str(urls[counter])
    b = a.replace("thumbnail", "user_image")
    c = b.replace("_s", "")
    urls[counter] = c
    counter += 1


# downloads and saves image to a specified folder with a specified name
def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


n = 0
for i in urls:
    print(i)
    url = i
    file_name = str(n)
    dl_jpg(url, file_path, file_name)
    n += 1
