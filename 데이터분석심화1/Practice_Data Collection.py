# -*- coding: utf-8 -*-
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

# # Practice : Data Collection

import pandas as pd
a=pd.io.parsers.read_csv('Connections_UK.csv')

print(a)

#데이터프레임 형식으로 만들기
df=a
df.head()











import pandas as pd
a=pd.ExcelFile('FranceMarketData.xlsx')
market=a.parse('sheet1',index_col=None,na_values=['NA'])
print(market)





# ### FROM THE WEB Practice

from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file=("https://upload.wikimedia.org/wikipedia/commons/4/4f/Felis_silvestris_catus_lying_on_rice_straw.jpg")
image=imread(example_file)
plt.imshow(image)
plt.show()

image2=image[500:1700,2500:3500]
plt.imshow(image2,cmap=cm.gray)
plt.show()

image3=resize(image,(1500,2500),mode='symmetric')
plt.imshow(image3,cmap=cm.gray)
print("data type: %s,shape:%s"%(type(image3),image3.shape))

image=imread(example_file, as_gray=True)
plt.imshow(image,cmap=cm.gray)

import pandas as pd
import numpy as np

a=pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_smartphone_penetration')

a

len(a)

df2=a[0]
df2

df2['Total population']=df2['Total population'].str.strip('m')
df2['Smartphone penetration']=df2['Smartphone penetration'].str.strip('%')
df2['Smartphone users']=df2['Smartphone users'].str.strip('m')
df2



# ## FROM THE WEB Practice

import newspaper
site=newspaper.build("https://www.techspot.com/")
site.article_urls()

site_article=site.articles[0]


site_article.download()

site_article.parse()

site_article.title


site_article.url

site_article.publish_date

site_article.text

import newspaper
from newspaper import Article
article=Article("https://www.etnews.com/20210702000137?mc=em_001_00001")
article.download()
article.parse()

article.title

print(article.text)

article.publish_date

# ### NEWS SCRAPING FROM THE WEB

import urllib.request as ure
from bs4 import BeautifulSoup as bs

news='https://www.bbc.com/'
soup=bs(ure.urlopen(news).read(),'html.parser')

soup.find_all('a',{"class":"happening__title"})

for i in soup.find_all('a',{"class":"happening__title"}):
                            print(i.text)

for i in soup.find_all('a',{"class":"happening__title"}):
    print(i.get('href'))

article1='https://www.bbc.com'
soup2=bs(ure.urlopen(article1).read(),'html.parser')

for i in soup2.find_all('module module -- header'):
    print(i.text)

print(soup2.find_all('module module -- header'))






