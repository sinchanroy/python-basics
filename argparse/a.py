
import argparse

def input():
    parser = argparse.ArgumentParser("Taking Inputs")
    parser.add_argument('--input', action='store', type=int, required=True)

    args = parser.parse_known_args()

    print(args.input)

if __name__ == '__main__':
    input()

