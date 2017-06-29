#!/usr/bin/env python

import sys

MIN_LETTERS = 5

def main():
    required_char = sys.argv[1].lower()
    required_chars = set(sys.argv[2].lower())
    this_file = set(open(sys.argv[3], "r").read().splitlines())
    for line in sorted([x for x in this_file if len(x) >= MIN_LETTERS and required_char in x and set(x).issubset(required_chars)]):
        print line


if __name__ == "__main__":
    main()
