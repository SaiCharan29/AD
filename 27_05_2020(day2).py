# -*- coding: utf-8 -*-
"""27-05-2020(Day2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c1mGOxi1B9GcOu4MKheO4KYYlirL0lKJ

# Python
## Python
### Python
#### Python
##### Python
###### Python

# Ordered List
1. List Item1
2. List Item2
3. List Item3

# UnOrdered List
- List Item1
    - Item 1
    - Item2
- List Item2
- List Item3

**Bold**
*Italic*

[Click here](https://moodle.dspsinstitute.com/)

![image](https://thumbs.dreamstime.com/b/internship-concept-chart-keywords-icons-50410024.jpg)

<img src="https://thumbs.dreamstime.com/b/internship-concept-chart-keywords-icons-50410024.jpg" width=600 height=400>
"""

a=2
b=2.4
c=2+3j
d="py"
print(type(a),type(b),type(c),type(d))

c1=4+5j
c2=complex(2,3)
print(c1+c2,c1.real,c1.imag)

a=int(input("Enter a value "))
b=int(input("Enter a value "))
print("sum=",a+b)

a=input()
print("Welcome "+a+"!!")

a=15
b=6
print(a+b,end=" ")
print(a-b)
print(a+b,a-b)
print(a+b,a-b,sep=", ")

a=15
b=6
print(a+b,a-b,a*b,a/b,a%b,a//b,a**b,sep=', ')

a=3
b=6
print(a<b,a>b,a<=b,a>=b,a==b,a!=b,sep=', ')

print(a<b and a!=b,a>b or a!=b , not a ,sep=', ')

li=[1,2,3,4]
print(1 in li, 5 in li, 3 not in li, sep=",")

if a<b:
  print(a,"is smaller than",b)
elif a>b:
  print(b,"is smaller than",a)
else:
  print("both are equal")

a=3
b=6
c=2
if a>b and a>c:
  print(a,"is largest")
elif b>c:
  print(b,"is largest")
else:
  print(c,"is largest")

n=int(input())
i=0
while(i<n):
  print("Py")
  i+=1

