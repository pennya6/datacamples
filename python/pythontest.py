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

# # python practice

# ## 2021-06-29 practice

print("Hello world")

a="restart"
b=a[1:]
a[0]+b.replace("r","$")


day=11
month=12
year=2014
print(f"The exmination will start from : {day}/{month}/{year}")

a="python"
len(a)
print(a[0])
print(a[2])
print(a[4])




# ### 2-3 practice

a=[2,3,4,['a',['Life','is','good'],['apple']]]
a[3][1][2]
a[3][2][0]

a=[1,2,3,4,5]
b=a[1:3]
print(b)

# ### 2-4 practice

line_up=[]
line_up.append('거북이')
line_up.append('홍학')
line_up.append('토끼')
line_up.sort()
print(line_up)

train=['성진','찬경','준영']
train.append('주아')
print("서울역 도착, //",train)
train.insert(0,'동빈')
print("대전역도착, //",train)
train.sort()
print("부산역 도착, //",train)


# +
#2-4 practice
# -

a=['Windows','macOS','Linux']
a.reverse()
a

b=['Python','Java','C++','Ruby','C']
b.pop(2)
b



#

# ## 2021-06-30 practice

# ### 2-5 practice

my_dict={'name':'Elli','age':37}
print(my_dict.get('name'))
print(my_dict.get('nokey'))
print(my_dict.get('age'))
list(my_dict.keys()).pop()

my_dict={'name':'Eile','age':37}
my_dict['address']='Downtown'
my_dict



# ### 2-6 pracitce

my_set={1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(4)
print(my_set)
my_set.update([5,6,8])
print(my_set)

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A&B)
print(A-B)



# ### 3-1 practice

a=33
b=200
if(b>a):
    print("b is greater than a")
else:
    print("NOPE")

a=33
b=33
if(b>a):
    print("b is greater than a")
elif(a==b):
    print("a and b are equal")

a=200
b=33
if(b>a):
    print("b is greater than a")
elif(a==b):
    print("a and b are equal")
else:
    print("a is greater than b")

a=200
b=33
c=500
if(a>b and c>a):
    print("Both conditions are True")

a=200
b=33
c=500
if(a>b or a>c):
    print("At leaet one of the conditions is True")



# ### 3-2 practice

Fruits=["apple","banana","cherry"]
for i in range(0,3):
    print(Fruits[i])

Fruits=["apple","banana","cherry"]
for i in range(0,3):
    if(Fruits[i]=="banana"):
        print("banana break")
        break

# ?? 타입이 리스트내포를 사용하면 리스트로 나오고
# 일반 for문을 사용하면 요소로 나오는가?
# 그렇다면 추후에 이 데이터를 사용하기 위해서는 리스트내포를 사용하는것이 좋은것인가?
#
# 리스트 내포는 새로운 리스트를 선언하는 경우에만 가능한 것인가?
#
# for문을 사용하는 경우에 a에서 다른 리스트로 옮기는 경우만 사용하는 건가?
# 자른다고 생각하면 안되는 건가?

a="human"
for i in range(0,len(a)):
    print(a[i])

a="human"
result=[a[i] for i in range(0,len(a))]
print(result)



result1=["human"]
result2="nice"
result=[result1.append(result2) for i in range(0,len(result1))]
print(result1)



for i in range(20):
    if(i%2==0):
        print(i)


result=[i for i in range(20) if(i%2==0)]
print(result)

result=[i for i in range(100)if(i%2==0 and i%5==0)]
print(result)



# ### 4-1 practice

def check(a,i):
    if(a[i]!='e' and a[i]!='s'):
         return print("Current letter : " + a[i])
a='estheresther'
for x in range(len(a)):
    check(a,x)


def check(a,b):
    if(b>a):
        print("b is greater than a")
check(a=33,b=200)


# +
def check(a,b):
    if(b>a):
        print("b is greater than a")
    elif(a==b):
        print("a and b are equal")
        
check(a=33,b=33)


# -

def check(a,b):
    if(b>a):
        print("b is greater than a")
    elif(a==b):
        print("a and b are equal")
    else:
        print("a is greater than b")
check(a=200,b=33)


def check(a,b,c):
    if(a>b and c>a):
        print("Both conditions are True")
check(200,33,500)


def check(a,b,c):
    if(a>b or a>c):
        print("At least one of the conditions is True")
check(200,33,500)


# +
def check(a):
    for i in range(len(a)):
        print(a[i])
    
a=["apple","banana","cherry"]
check(a)


# -

def check(a):
    result=[a[i] for i in range(len(a)) if(a[i]!='banana')]
    return result
a=["apple","banana","cherry"]
check(a)


def check(a):
    result=[a[i] for i in range(len(a))]
    return result
a="human"
check(a)



# ## 2021-07-01 practice

# ### 4-1 practice

x=lambda a : a+10
result=x(10)
result

test= lambda a,b : a*b
result=test(10,10)
result

test=lambda a,b,c: a+b+c
result=test(1,2,3)
result

test=lambda a:a**3 if a%2==0 else a**2
result=test(4)
result

test=lambda a: a**3 if a%2==0 else (a**4 if a%3==1 else a**2)
result=test(3)
result



# ### 4-2 practice

a=input()

a

a=input()
b=input()
test=lambda a,b: a*b
x=int(float(a))
y=int(float(b))
print(test(x,y))

# +
a=input()
b=input()
x=input("기호를 입력하시오:")

p=int(float(a))
y=int(float(b))

if(x=="*"):
    print(p*y)
elif(x=="%"):
    print(p%y)
elif(x=="/"):
    print(p/y)
elif(x=="+"):
    print(p+y)
elif(x=="-"):
    print(p-y)
else:
    print("오류")
# -

user_list=["sohyun","jayoung","miyoung","jihyun","heeyoung"]
print(user_list)
person=input("이름을 입력하세요: ")
x=len(user_list)
print(x)
for i in range(x):
    if(user_list[i]==person):
        del user_list[i]
        x-=1
while(x>1):
    person2=input("생일, 전화번호, 나이, 성별을 입력하세요 : ")
    print(person2)
    break



# ### 4-3 practice

f= open("C:/Users/user/Desktop/데청캠/Pythontest/testfile.txt","w")
f.write(input())
f.close()

with open("C:/Users/user/Desktop/데청캠/Pythontest/testfile.txt","w") as f:
    f.write(input())
f.close()

f= open("C:/Users/user/Desktop/데청캠/Pythontest/test.txt","a")
f.write(input())
print("Update File")
f2=open("C:/Users/user/Desktop/데청캠/Pythontest/test.txt","r")
data=f2.read()
print(data)
f.close()
f2.close()

with open("C:/Users/user/Desktop/데청캠/Pythontest/test.txt","a") as f2:
    f2.write(input())
print("Update File")
with open("C:/Users/user/Desktop/데청캠/Pythontest/test.txt","r") as f:
    data=f.read()
print(data)
f.close()



# ### 5-1 practice

# +
class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    
a=FourCal()
a.setdata(4,2)
print(a.mul())
print(a.div())
print(a.sub())
print(a.add())


# +
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    
a=FourCal(4,2)
print(a.mul())
print(a.div())
print(a.sub())
print(a.add())
# -




































