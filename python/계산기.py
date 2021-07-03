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

# ### 연습문제2

# 프로그램 : 사용자로부터 n개의 사칙연산 기호를 받아서 연산 수행
#
# 순서
# 1: 사칙연산 기능 구현
# 2: 제어문 -> while문으로 입력 받기 만 false인 경우 break
# 3: reset 함수 구현 -> 숫자 0를 입력하면 초기화
# 4: 연산 우선 순위 적용 
# -> 리스트 두개 생성 
#     a[] : 숫자
#     b[] : 연산 기호
#     for문으로 b[]에서 *,/ 가 나오면 해당 인덱스(i)의 a[i],a[i+1] 먼저 계산 -> 그리고 결과값은 인덱스 i
#     
#     
# -> 리스트 1개
# input 한줄로 받아서 split하고 만약에 split하다가 *,/가 나오면 계산한다
# 이후에 없으면 앞에서 부터 +,- 계산
# = 가 나오면 계산 시작

# +
a=input("계산를 입력하세요")
x=len(a)

for i in range(x):
    if(a[i]=="="):
        print("계산 시작")
    elif(a[i]=="+"):
        a[i-1]=int(float(a[i-1]))
        a[i+1]=int(float(a[i+1]))
        a[i-1]=sum(a[i-1],a[i+1])
       # a[i]=sum(int(a[i-1]),int(a[i+1]))
        
print(a)
#사칙연산 수행 기능 함수
#더하기
def sum(a,b):
    return a+b
#빼기
def sub(a,b):
    return a-b

#곱하기
def mul(a,b):
    return a*b

#나누기
def sksnrl(a,b):
    return a/b
# -



# +
# str int값으로 변환
def change(a):
    a=int(float(a))
    return a

#사칙연산 수행 기능 함수
#더하기
def add(a,b):
    return a+b
#빼기
def sub(a,b):
    return a-b

#곱하기
def mul(a,b):
    return a*b

#나누기
def sksnrl(a,b):
    return a/b


a=input("계산 할 숫자를 입력하세요(종료하고 싶다면 false를 입력하세요)")

#사용자에게 숫자 입력받기

x=len(a)    
for i in range(x):
    if(a[i]=='false'):
        print("종료")
        break
    elif(a[i]=="="):
        print("계산 시작")
    elif(a[i]=="*"):
        change(a[i-1])
        change(a[i+1])
        a[i-1]=mul(a[i-1],a[i+1])
        # 계산한 숫자와 연산 삭제
        del a[i]
        del a[i+1]
    elif(a[i]=="/"):
        change(a[i-1])
        change(a[i+1])
        a[i-1]=sksnrl(a[i-1],a[i+1])
        # 계산한 숫자와 연산 삭제
        del a[i]
        del a[i+1]
    else:
        print("우선 순위 기호 없음")
        
print(a)

y=len(a)
for i in range (y):
    if(a[i]=="-"):
        change(a[i-1])
        change(a[i+1])
        a[i-1]=sub(a[i-1],a[i+1])
        # 계산한 숫자와 연산 삭제
        del a[i]
        del a[i+1]
    elif(a[i]=="+"):
        change(a[i-1])
        change(a[i+1])
        a[i-1]=add(a[i-1],a[i+1])
        # 계산한 숫자와 연산 삭제
        del a[i]
        del a[i+1]
    else:
        print("계산종료")


print(a)
# -




