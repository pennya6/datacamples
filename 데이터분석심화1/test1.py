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

# ## Colors.txt open

with open("Colors.txt",'r') as open_file:
    print('Colors.txt content:\n'+open_file.read())

import matplotlib.image as img
import matplotlib.pyplot as plt
image=img.imread("MySamplePlot.png")

print(image.shape)
print(image.size)
plt.imshow(image)
plt.show()

# +
# 한줄씩 나오게 하기

with open("Colors.txt",'r')as open_file:
    for observation in open_file:
        print('Reading Data: '+observation)
# -

#짝수번째 줄만 불러오기 
n=2
with open("Colors.txt",'r') as open_file:
    for j, observation in enumerate(open_file):
        if j%n==0:
            print('Reading Line: '+str(j)+' Content: '+observation)

# +
#pandas을 이용한 데이터프레임 형식으로 만들기

import pandas as pd
color_table=pd.io.parsers.read_table("Colors.txt")
print(color_table)

# +
#csv 파일 읽어와 데이터프레임으로 만들기

import pandas as pd
titanic =pd.io.parsers.read_csv("Titanic.csv")
print(titanic)
# -

X=titanic[['age']]
print(X)

import pandas as pd


xls=pd.ExcelFile("Values.xls")  #xls파일을 pd로 바꾸기
trig_values=xls.parse('Sheet1',index_col=None, na_values=['NA'])
print(trig_values)

# +
import xml.etree.ElementTree as et
import pandas as pd

xtree=et.pandas("XMLData.xml")
xroot=xtree.getroot()
df_cols=["Number","String","Boolean"]
rows=[]
# -

for node in xroot:
    s_num=node.find("Number").text if node is not None else None
    s_str=node.fine("String").text if node is not None else None
    s_bool=node.find("Boolean").text if node is not None else None
    
    rows.append({"Number":s_num,"String":s_str,"Boolean":s_bool})

out_df=pd.DataFrame(rows,columns=df_cols)
print(out_df)
























