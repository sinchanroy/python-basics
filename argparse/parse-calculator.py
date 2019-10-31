#! /usr/bin/env python

import argparse

if __name__ == '__main__':
 parser = argparse.ArgumentParser("Description : Short Sample App")
 parser.add_argument('-a', type=int, help="number1")
 parser.add_argument('-b', type=int, help="number2")
 parser.add_argument('-operation', help="operation to perform")
 args = parser.parse_args()
 if (args.operation == "add"):
  print (" \n Sum is ", int(args.a + args.b), "\n")
 elif (args.operation == "substract"):
  print ("\n Difference is ", int(args.a - args.b), "\n")
 elif (args.operation == "multiply"):
  print ("\n Product is ", int(args.a * args.b), "\n")
 elif (args.operation == "division"):
  print ("\n Quotient is ", int(args.a / args.b), " and remainder is ", int (args.a % args.b), "\n" ) 
 else:
  print("Invalid option")

