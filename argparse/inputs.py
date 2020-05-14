import argparse

def input():
 parser = argparse.ArgumentParser(description="Process some integers")
 parser.add_argument('--one', help='take inputs')
 parser.add_argument('--two',  help ="take second input")
 args = parser.parse_args()
 return args

def display(args):
 input = int(str(args.one)+str(args.two))
 print(args.one)
 print(args.two)
 print(input)
 
if __name__ == '__main__':
 args = input()
 display(args)
