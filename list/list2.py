#! /usr/bin/env python 

arr = []

total = int(input("Enter total Array Elements : "))

print("Enter array elements : ")

for i in range (0,total):
 arr.append(int(input()))

print(arr)

num=int(input("Enter the position you would like to delete : "))
arr1 = [] 
arr1=arr.pop[num]

print(arr1)
