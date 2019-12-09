#! /usr/bin/env python 

def fibo(num):
  first = 0
  second = 1
  arr = []
  arr.append(first)
  arr.append(second)
  for i in range (num-2): 
    third = first + second
    first = second
    second = third
    arr.append(third)
  print("Series is : " + str(arr)) 

def lamda(num):
  first = 0
  second = 1
  arr = []
  arr1 = []
  arr.append(first)
  arr.append(second)
  arr1 = lambda first,second : third = first + second \ 
         first = second \ 

if __name__ == '__main__':
  total = int(input("Enter total number of elementi : "))
  choice = int(input("Do you want to calculate in 1> Normal Function or 2> Lambda Function or 3> Lambda&Map Function "))
  if (choice == 1):
    fibo(total)
  else:
    arr = lamda(total)
 



