# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
# parses the html text
from urllib.request import urlopen
# grabs the page itself

amazon_url="https://www.amazon.in/Smartphones/b?ie=UTF8&node=1805560031"
urlconn=urlopen(amazon_url)
page_html=urlconn.read()
urlconn.close()
page_soup=soup(page_html,"html.parser")
#print(page_soup.h1)

containers = page_soup.findAll("div",{"class":"crwBucket"})
print(len(containers))
#print(containers[0])
# http://jsbeautifier.org/

filename="amazon.csv"
f=open(filename,"w")
headers = "product,rating,price\n"
f.write(headers)

for container in containers:
    product=container.div.img["title"]
    product=product.replace(',','')
    rating=container.findAll("span",{"class":"a-icon-alt"})[0].text
    price=container.findAll("span",{"class":"crwActualPrice"})[0].text
    price=price.replace(',','')
    print(product+","+rating+","+price+","+rating.split(' ')[0]+","+price.split(' ')[-1])
    f.write(product+","+rating+","+price+","+rating.split(' ')[0]+","+price.split(' ')[-1]+"\n")

f.close()
    