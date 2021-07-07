# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 2021-07-07 practice

from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file=("http://upload.wikimedia.org/wikipedia/commons/7/7d/Dog_face.png")
image=imread(example_file)
plt.imshow(image)
plt.show()

image2=image[5:70,0:70]
plt.imshow(image2,cmap=cm.gray)
plt.show()

image3=resize(image2,(30,30),mode='symmetric')
plt.imshow(image3,cmap=cm.gray)
print("data type : %s,shape:%s"%(type(image3),image3.shape))

# ### tabular data from the web

# +
import pandas as pd
import numpy as np

table_PA=pd.read_html('https://en.wikipedia.org/wiki/Politics _of_Pennsylvania')
# -
df=table_PA[0]
df.head()

df['Democratic']=df['Democratic'].str[:4]

# +
import newspaper
from newspaper import Article

article=Article("https://www.3gpp.org/news-events/2143-3gpp-meets-imt-2020")
article.download()
article.parse()
print(article.text)
# -
article.title

article.authors

import newspaper
site=newspaper.build("https://techcrunch.com/")
site.article_urls()

site_article=site.articles[0]
site_article.download()
site_article.parse()
site_article.title
site_article.url

allarticles=[]
for i in range(len(site.article_urls())):
    article=Article(site.article_urls()[i])
    article.download()
    article.parse()
    allarticles.append(article)

import pandas as pd
df=pd.DataFrame(columns=['Title','Authors','PubDate','URL','Text'])

for i in range(len(allarticles)):
    row=dict(zip(['Title','Authors','PubDate','URL','Text'],[allarticles[i].title,allarticles[i].authors,allarticles[i].public_date,allarticles[i].urls,allarticles[i].text]))
    row_s=pd.Series(row)
    row_s.name=i
    df=df.append(row_s)
df

import urllib.request as ure
from bs4 import BeautifulSoup as bs

news='https://www.forbes.com/'
soup=bs(ure.urlopen(news).read(),'html.parser')

soup.find_all('a',{"class":"happening__title"})

for i in soup.find_all('a',{"class":"happening__title"}):
    print(i.text)

for i in soup.find_all('a',{"class":"happening__title"}):
    print(i.get('href'))

article1="https://www.forbes.com/sites/siladityaray/2021/07/06/us-lawyer-handed-prison-sentence-in-hong-kong-over-scuffle-with-police-during-2019-protests/?sh=ff8d6ab3adea"
soup2=bs(ure.urlopen(article1).read(),'html.parser')

for i in soup2.find_all('p'):
    print(i.text)

happening=soup.find_all('a',{"class":"happening__title"})

rows=[]
for i in range(len(happening)):
    happeningtitle=happening[i].text
    happeningurl=happening[i].get('href')
    soup2=bs(ure.urlopen(happeningurl).read(),'html.parser')
    txt=""
    for j in soup2.find_all('p'):
        txt=txt+j.text
    rows.append({'Title':happeningtitle,'URL':happeningurl,'Text':txt})

import pandas as pd
df= pd.DataFrame(rows,columns=['Title','URL','Text'])
df






