#webscraping with python
# request
# bs4
# pandas
# json
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests

#website url
url="https://www.imdb.com/chart/top/"
#req and content of website
res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')

titles=soup.find_all('td',class_='titleColumn')
rating=soup.find_all('td',class_='ratingColumn imdbRating')
images=soup.find_all('td',class_='posterColumn')



title=[]
ratings=[]
img=[]

for t in titles:
    title.append(t.text)
for r in rating:
    ratings.append(r.text)
for i in images:
    p=i.img['src']
    img.append(p)

d={'titles':title,'ratings':ratings,"img":img}


d1=json.dumps(d)
l=json.loads(d1)

with open('movies.json','w') as f:
    f.write(d1)
    f.close()
print("success")


#bikedekho
#flipkart