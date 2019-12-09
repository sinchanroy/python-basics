#! /usr/bin/env python 

import logging 

def division (num1,num2):
 return num1/num2

def addition (num1,num2):
 return num1+num2

def substraction (num1,num2):
 return num1-num2

def multiplication (num1,num2):
 return num1*num2

def accept ():
 
 format = '%(asctime)s %(message)s'
 logging.basicConfig(level=logging.DEBUG, filename='/tmp/test.log', datefmt='%a, %d %b %Y %H:%M:%S')
 logging.critical("Starting debug")
 
 a = int(input("Enter number 1 : "))
 b = int(input("Enter number 2 : "))
 op = str(input("Enter operation (add/sub/div/mul) : "))
 logging.warning(op)
 
 if op == "add":
  logging.debug("Sum is " + str(addition(a,b)))
 
 elif op == 'sub':
  logging.warning("Difference is " + str(substraction(a,b)))
 
 elif op == 'mul':
  logging.info("Product is " + str(multiplication(a,b)))
 
 elif op == 'div':
  logging.critical("Quotient  is " + str(division(a,b)))
 
 else:
  logging.error("Invalid argument")

 logging.critical("Stopping debug")

if __name__ == '__main__':
 accept()



 





