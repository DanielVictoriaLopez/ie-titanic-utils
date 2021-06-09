import sys

from ie_utils import tokenize

def main():
    print(tokenize("Hello world"))

if __name__ == "__main__":
    main()

if str(sys.argv[1]):
    print(tokenize(str(sys.argv[1])))