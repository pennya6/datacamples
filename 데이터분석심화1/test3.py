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

# # DATA PROCESSING PRACTICE

from pandas import read_csv

dataset = read_csv('pima-indians-diabetes.csv',header=None)
dataset

print(dataset.describe())

num_missing = (dataset[[1,2,3,4,5]] == 0).sum()
print(num_missing)

from numpy import nan
dataset = read_csv('pima-indians-diabetes.csv', header = None)
datasetorig = dataset.copy()
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, nan)
print(dataset.head(10))
print(datasetorig.head(10))

dataset.dropna(inplace=True)

print(dataset.shape)

print(datasetorig.shape)

dataset = read_csv('pima-indians-diabetes.csv', header = None)
datasetorig = dataset.copy()
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, nan)

from sklearn.impute import SimpleImputer
import pandas as pd
values = dataset.values
imputer = SimpleImputer(missing_values=nan, strategy='mean')
dataimputed=pd.DataFrame(imputer.fit_transform(values))

print(values )

print(dataimputed)

import pandas as pd
import numpy as np
dataset = pd.read_csv('pima-indians-diabetes.csv', header = None)
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, np.nan)

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer()
datatrans=pd.DataFrame(imputer.fit_transform(dataset))

from missingpy import MissForest
imputer = MissForest()
datatrans = pd.DataFrame(imputer.fit_transform(dataset))

from sklearn.impute import KNNImputer
imputer = KNNImputer()
datatrans = pd.DataFrame(imputer.fit_transform(dataset))

datasetorig.columns = datasetorig.columns.map(str)
newnames = {'0':'num_preg', '1':'gluc_concent', '2':'blood_press',
'3':'thickness', '4':'ser_insulin', '5':'bmi', '6':'diab_pedi',
'7':'age', '8':'clas'}
datasetorig.rename(columns=newnames,inplace=True)
datasetorig

d = { 'Letter':['a','b','c','d','e','e',
'f','g','h','i','j','k','l','l','l','m','m','n','o','o'],'Index':[1
,2,3,4,5,5,6,7,8,9,10,11,12,12,12,13,13,14,15,15]}
df = pd.DataFrame(d,columns=['Letter','Index'])
df


df.drop_duplicates()

df = pd.read_csv('BL-Flickr-Images-Book.csv', encoding='cp949')

from numpy import nan
dataset = read_csv('pima-indians-diabetes.csv', header = None)
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, nan)
dataset.dropna(inplace=True)

datablbm = dataset[{2,5}]

from sklearn.preprocessing import MinMaxScaler
trans = MinMaxScaler()
blbmmm = trans.fit_transform(datablbm)
blbm = pd.DataFrame(blbmmm)

print (blbm)
print (blbmmm)

from sklearn.preprocessing import StandardScaler
trans = StandardScaler()
blbmn = trans.fit_transform(datablbm)
blbmnorm = pd.DataFrame(blbmn)

heiwei = read_csv('weight-height.csv')
heiwei['Heightc']=2.54*heiwei['Height']/100
heiwei['Weightk']=0.453592*heiwei['Weight']
print(heiwei)

heiwei['BMI']=heiwei['Weightk']/(heiwei['Heightc']**2)
print(heiwei)

sales = read_csv('salesdaily.csv')
sales['datum']= pd.to_datetime(sales['datum'])
sales.set_index('datum', inplace=True)
print(sales)

salesm = sales.resample('M').sum()
salesq = sales.resample('Q').sum()
salesa = sales.resample('A').sum()

print(salesm)

print(salesq)

print(salesa)







addr = ['London', 'Oxford', 'Coventry', 'Tyre', 'York']
a = df['Place of Publication'].str.contains('|'.join(addr))

for i in df.index:
if a[i] == True:
df['Place of Publication'][i] = "United Kingdom"
else:
pass 

eqw = pd.cut(heiwei['BMI'], bins = 4)
print(eqw)

eqf = pd.qcut(heiwei['BMI'], q=4)
print(eqf)

from numpy import array
from numpy import diag
from numpy import zeros
from scipy.linalg import svd
A =array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[51,52,53,54,55,56,57,58,59,60]])
print(A)

U, s, VT = svd(A)
smatrix = zeros((len(s), len(s)))
smatrix[:len(s),:len(s)] = diag(s)
print(smatrix)

print(diag(s))

k=4
smatrix = smatrix[:k, :k]
VT = VT[:k, :]
U = U[:,:k]
B = U.dot(smatrix.dot(VT))
print(B)

k=3
smatrix = smatrix[:k, :k]
VT = VT[:k, :]
U = U[:,:k]
B = U.dot(smatrix.dot(VT))
print(B)

from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
iris = datasets.load_iris()
labels = pd.DataFrame(iris.target)
labels.columns=['labels']
data = pd.DataFrame(iris.data,columns=['Sepal length','Sepal width','Petal length','Petal width'])

fig = plt.figure( figsize=(6,6))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(data['Sepal length'],data['Sepal width'],data['Petal length'],c=labels,alpha=0.5)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
plt.show()

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
scaler = StandardScaler()
pca = PCA()
pipeline = make_pipeline(scaler,pca)
pipeline.fit(data)

from sklearn.decomposition import PCA
import pandas as pd
print(pca.explained_variance_ratio_)
print(pd.DataFrame(pca.components_,columns=iris.feature_names))
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()

model = PCA(n_components=2)
pca_features = model.fit_transform(data)
xf = pca_features[:,0]
yf = pca_features[:,1]
plt.scatter(xf,yf,c=iris.target);
plt.show()

#히스토그램 그리기
data.hist()

data['Sepal length'].hist()

#iris 데이터 로딩
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
data = pd.DataFrame(iris.data,columns=['Sepal length','Sepal width','Petal length','Petal width'])
data

#15개지정해서 샘플링
samn = data.sample(n=15, random_state=1000)
samf = data.sample(frac=0.1, random_state=1000)
samn

#10프로 샘플링
samn

#중복되어서 샘플링 가능
samwr = data.sample(n=15, replace=True, random_state=1000)
samwr














