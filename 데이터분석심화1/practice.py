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

# # 2021-07-06 practice

# ## 데이터분석심화1

import numpy as np




np.array([1,2,3], dtype=np.int)
np.array([1,2,3], dtype=np.float)
np.array([1,2,3], dtype=np.complex)

np.zeros((2,3))

np.ones(4)

np.full(3,3.2)

data=np.ones(4)
data.fill(3)
data

np.arange(0,12,4)

np.linspace(0,12,4)

np.logspace(0,2,3)

x=np.array([-1,0,1])
y=np.array([-2,0,2])
x,y=np.meshgrid(x,y)
print(x)
print(y)

a=np.arange(0,11)
a[0]

a[-1]

a[4]

a[0:5]

a[0:5:2]

a[:5]

a[-5:]

a[::-2]

a=np.array([[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]])


a[:,1]

a[1,:]

a[:2,:2]

a[::2,::2]

a[1::2,1::2]

A=np.linspace(0,1,11)
A[np.array([0,2,4])]

A[A>0.5]

A[np.arange(2,5)]

data=np.array([[1,2],[3,4]])

np.reshape(data,(1,4))

data.flatten()

data=np.arange(5)
np.vstack((data,data,data))

np.hstack((data,data))

a=np.arange(3)
b=np.arange(4)
np.concatenate((a,b))

np.append(a,[3,4,5])

np.resize(b,(2,3))

np.cos(np.pi)

np.sin(np.pi)

np.tan(np.pi)

np.sqrt(4)

np.log2(8)

np.log10(100)

a=[1,2,3]
b=[2,4,6]
np.add(a,b)
np.subtract(b,a)
np.multiply(a,b)
np.divide(b,a)

np.power(2,3)
np.remainder(8,3)
np.reciprocal(0.5)
np.abs(-5.0)
np.sign(-5.0)
np.round(3.4124,2)

a=np.arange(0,10)
np.mean(a)

np.std(a)

np.var(a)

np.sum(a)

np.prod(a)

print(np.min(a),np.max(a))

np.argmin(a), np.argmax(a)

np.all(a)

np.any(a)

a=np.linspace(0,16,5)
a

# a가 5가 작을때 a 아니면 10 곱하기
np.where(a<5,a,10*a)

#a의 012
np.choose(2,a)

#0이 아닌 값을 구하라
np.nonzero(a)

#a<2이면 a-1, a>=2이면 a**2
np.select([a<2,a>=2],[a-1,a**2])

np.logical_and(a>1,a<10)

np.logical_or(a<1,a>15)

np.logical_not(a>5)

mat=np.arange(9).reshape(3,3)
mat

#대각선 기준으로 바꾸기
np.transpose(mat)

#중간 열을 기준으로 바꾸기
np.fliplr(mat)

#중간행 기준
np.flipud(mat)

np.rot90(mat)

A=np.arange(1,7).reshape(2,3)
B=np.arange(1,7).reshape(3,2)
A

np.dot(A,B)

np.outer(B,A)

c=[2,3,4]
d=[4,5,6]
np.inner(c,d)
np.cross(c,d)

# ## sympy

import sympy

x=sympy.Symbol("x")
y=sympy.Symbol("y")

expr=2*(x**2-x)-x*(x+1)
expr

expr=2*sympy.cos(x)*sympy.sin(x)
expr

expr=sympy.exp(x)*sympy.exp(y)
expr

expr=1/(x**2-1)+1/(x+1)
expr

a,b,c,d=sympy.symbols("a,b,c,d")
M=sympy.Matrix([[a,b],[c,d]])
M

M*M

x=sympy.Matrix(sympy.symbols("x_1,x_2"))
q=sympy.Matrix(sympy.symbols("q_1,q_2"))
x=M.inv()*q
sympy.solve(M*x-q,x)

sympy.transpose(M)

sympy.adjoint(M)

sympy.det(M)

sympy.trace(M)

M.inv()

N=sympy.Matrix([[-4,2],[6,7]])

N.LUdecomposition()

N.QRdecomposition()

N.diagonalize()

N.rank()












































