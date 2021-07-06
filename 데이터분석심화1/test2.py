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




