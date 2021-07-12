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

# ### Data processing practice

# #### 1

import pandas as pd

xls=pd.read_excel("rawdata.xlsx")
xls

num_missing = (xls[['Q1 2000','Q2 2000','Q3 2000','Q4 2000']] == 0).sum()
print(num_missing)

from numpy import nan

datasetorig = xls.copy()
xls[['Q1 2000','Q2 2000','Q3 2000','Q4 2000']] = xls[['Q1 2000','Q2 2000','Q3 2000','Q4 2000']].replace(0, nan)
xls.head(10)


datasetorig.head(10)

xls.dropna(inplace=True)

print(xls.shape)

print(datasetorig.shape)

xls.drop_duplicates()









# #### 2

from pandas import read_csv

dataset = read_csv('Forbes Top2000 2017.csv',header=None)
dataset

from numpy import nan
dataset[['Q1 2000','Q2 2000','Q3 2000','Q4 2000']] = dataset[['Q1 2000','Q2 2000','Q3 2000','Q4 2000']].replace(0, nan)



# #### 3

import pandas as pd

a=pd.read_excel("FranceMarketData.xlsx")
a

a.drop('Attribute',axis=1)

a.drop(['Metric','Attribute'],axis=1)

a['Market, Operator']

a.set_index('Unnamed: 5',implace=True)

a_sum=a['Unnamed: 5'].sum()











# #### 4

b=pd.read_excel("rawdata.xlsx")
b





# #### 5

# +
#컬럼에 들어있는 값 변경하기
# -

from pandas import read_csv

d = read_csv('Forbes Top2000 2017.csv',header=None)
d

# +
addr=['Information Technology','Telecommunication Services']
a=d[8].str.contains('|'.join(addr))

for i in d.index:
    if a[i]==True:
        d[8][i]="ICT"
    else:
        pass
# -

d

# +
addr2=['Energy','Utilities']
a2=d[8].str.contains('|'.join(addr2))

for i in d.index:
    if a2[i]==True:
        d[8][i]="Infra"
    else:
        pass
# -

d

# #### 6

from pandas as pd

f=pd.read_excel("rawdata.xlsx")
f

#2015년만 뽑아오기
eqw=pd.cut(f['Q1 2015'], bins=4)
eqw2=pd.cut(f['Q1 2015'], bins=8)
eqw3=pd.cut(f['Q1 2015'], bins=16)

eqw

eqw2

eqw3



# #### 7

#rawdata.xlsx
f

#NaN을 0으로 대체하기
from numpy import nan
import numpy as np
f=f.replace(np.nan,0)

f



# #### 8

f

f1=f['Q1 2015']

f2=f['Q2 2015']

f3=f['Q3 2015']

f4=f['Q4 2015']

f_sum=pd.concat([f1,f2],axis=1)

f_sum=pd.concat([f_sum,f3],axis=1)

f_sum=pd.concat([f_sum,f4],axis=1)

f_sum

f_sum.hist()

#이산형화
eqw=pd.qcut(f_sum['Q1 2015'],q=4)
eqw



# #### 9

#Forbes Top2000 2017.csv 파일
d

#500개의 샘플 뽑기
samn=d.sample(n=500,random_state=1000)
samn

#20퍼센트의 샘플링 뽑기
samf=d.sample(frac=0.2,random_state=1000)
samf










