import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

parser_a = subparser.add_parser("a")
parser_a.add_argument("-one")


b_parser = subparser.add_parser("b")
b_parser.add_argument("-two")

a_args = parser.parse_args()
b_args = parser.parse_args()

print(a_args.a)
print(b_args.b)




