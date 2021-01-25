from bs4 import BeautifulSoup
from lxml import html
import requests
import time
add="/test-sites/e-commerce/static"
url="https://webscraper.io"+str(add)
data=requests.get(url).text
soup=BeautifulSoup(data,'lxml')
menu=soup.find("ul", {"id": "side-menu"})
las=menu.find_all("a")
l=list()
for a in las :
    add=a.get('href')
    url="https://webscraper.io"+str(add)
    data=requests.get(url).text
    soup=BeautifulSoup(data,'lxml')
    articls=soup.find_all("a", {"class": "title"})
    for articl in articls :
        add=articl.get('href')
        url="https://webscraper.io"+str(add)
        data=requests.get(url).text
        soup=BeautifulSoup(data,'lxml')
        div=soup.find("div", {"class": "col-lg-10"})
        titels=div.find_all("h4")
        description=div.find("p", {"class": "description"})
        for titeli in titels :
            if titeli.has_attr('class')==False:
                titel=titeli.text
            else:
                price=titeli.text 
        element={}
        element['title']  =   titel
        element['price']  =   price
        element['description']  =   description.text
        l.append(element)         
print(l)