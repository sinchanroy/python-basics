import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# Radius Search
create_parser = subparsers.add_parser('radius', help='Create a directory')
create_parser.add_argument('--continentid', action='store', help='Continent ID')

# Region Search
delete_parser = subparsers.add_parser('region', help='Remove a directory')
delete_parser.add_argument('--latitude', action='store', help='Latitude')

args =  parser.parse_args()

print (args)

if args.continentid is None : 
 print(args.latitude)
else:
 print(args.continentid)
