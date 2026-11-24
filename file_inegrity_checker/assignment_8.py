#def introduce(name , age , proffesion):
   # print("name", name)
    #print("age" , age)
    #print("proffesion", proffesion)

#introduce("vanshika",18,"student of GLA University")


# def pythagoras(a,b):

#     return square(a) + square(b)
# c2 = pythagoras(3,4) 
# def square(x):
#     return x * x 
# print("c2 = ", c2)
# # error (square is called before degining)

# def local():
#     lang = "Python" 
#     print(lang)
# local()
# pyhton is output

# name = "Suyash" 
# def test():
#     print(name) 
#     lang = "Python" 
#     print(lang)
# test() 
# print(name)
#suyash
#python
#suyash


# name = "Suyash" 
# print(name)
# def test():
#     global name 
#     print(name)
#     name = "Chaudhary" 
#     print(name)
# test() 
# print(name)
#suyash
#suyash
#chaudhary
#chaudhary



# name = "abc" 
# print(name)
# def fun1():
#     name = "def" 
#     print(name)
# print(name) 
# fun1()
# def fun2():
#     global name 
#     name = "ghi" 
#     print(name)
# print(name) 
# fun2() 
# print(name)
# abc
# abc
# def
# abc
# ghi
# ghi

# def fun1():
#     name = "Suyash" 
#     def fun2():
#         name = "Chaudhary"

#     fun2()
#     print(name) 
# fun1()
# suyash


# def fun1():
#     name = "Suyash" 
#     def fun2():
#         nonlocal name
#         name = "Chaudhary" 
#     fun2()
#     print(name) 
# fun1()
# chaudhary


# square of a number using lambda function
# sq = lambda a: a*a
# a = int(input("enter the number"))
# print("square of the given number is ",sq(a))
# input 7
# square of the given number is 49


# even and odd no with lambda function
# even_odd_no = lambda a: "even" if a%2==0 else "odd"
# a = int(input("enter the number"))
# print("number is ",even_odd_no(a))
# input 6
# number is even

#max of two no using lambda function
# max_no = lambda a,b: a if a>b else b
# a = int(input())
# b = int(input())
# print("max between two:", max_no(a,b))
# input 1
# input 2
# max between two: 2


# max of three no using lambda function
# max_no = lambda a,b,c: a if a>b and a>c else b if b>c else c
# a, b, c = map(int, input().split())
# print("max among three:",max_no(a,b,c))
# input 1 2 3
# max among three: 3


#filter even no from the list using functions
# def ftr(a):
#     even_no = []
#     for i in range(len(a)):
#         if a[i]%2==0:
#             even_no.append(a[i])
#     return even_no
# a = list(map(int,input().split()))
# print(ftr(a))

# this by using filter function
# def fun(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False
# a = list(map(int,input().split()))
# filtered = list(filter(fun,a))
# print(filtered)

# filtering even no from a list by. using lambda and filter function
# a = list(map(int,input().split()))
# filter = list(filter(lambda a: a%2==0,a))
# print(filter)


# check whether the no is prime no or not using function
# def prime_no(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
#     else:
#         return False
# n = int(input())
# print(prime_no(n))

#for a given array, count the no of elements having atleast one element greater then itself
# d1 _greater(arr))

# arr = list(map(int,input().split()))
# n = int(input())
# count = 0
# for i in range(len(arr)):
#     if arr[i]<=n:
#         count += 1
# print(count)

# n = list(map(int,input().split()))
# target = int(input())
# for i in range(len(n)):
#     for j in range(len(n)):
#         if n[i]+n[j]==target and i!=j:
#             print(i,j)

# with function
# def index_of_sum(n,target):
#     for i in range(len(n)):
#         for j in range(len(n)):
#             if n[i]+n[j]==target and i!=j:
#                 return (i,j)
# n = list(map(int,input().split()))
# target = int(input())
# print(index_of_sum(n,target))

# finding the element that appears only once in the list og no.
# def single_no(arr):
#     for i in range(len(arr)):
#         if arr.count(arr[i]) == 1:
#             return arr[i]
# arr = list(map(int,input().split()))
# print(single_no(arr))


# finding the element that appears only once in the list og no.using XOR operator
# def single_no(arr):
#     a = 0
#     for i in range(len(arr)):
#         a ^= arr[i]
#     return a
# arr = list(map(int,input().split()))
# print(single_no(arr))

# creating lowercase using lambda function
# lowercase = lambda a: a.lower()
# a = str(map(str,input().split()))
# print("lowercase of the given string is:",lowercase(a))



# a = list(map(int,input().split()))
# num = list(filter(lambda a: a>=60,a))
# print(num)

# a = list(map(int,input().split()))
# add = list(map(lambda a: a+10,a))
# print(add)

a = list(map(str,input().split()))
lower = list(map(lambda a: a.lower(),a))
lower = " ".join(lower)
print(lower)