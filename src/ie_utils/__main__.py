import sys

from ie_utils import tokenize

import argparse

parser = argparse.ArgumentParser(description='IE Tokenizer.')
parser.add_argument('sentence', metavar='sentence', type=str,
                    help='Sentence to parse')

args = parser.parse_args().sentence

def main():
    print(tokenize(args))

if __name__ == "__main__":
    main()