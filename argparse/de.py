import argparse
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

parser_a = subparser.add_parser("a")
parser_a.add_argument("-x")

args= parser.parse_args()

print (args.x)
