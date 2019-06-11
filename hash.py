#!/usr/bin/env python
# hash.py
#
# Takes raw text from STDIN, prints hashed data to STDOUT. Defaults to sha-256.

import argparse
import hashlib


hash_algos = hashlib.algorithms_available

parser = argparse.ArgumentParser(description="Hash raw text data from STDIN.")

parser.add_argument("-a", "--algo",
                    type=str,
                    dest="hash_algo",
                    choices=hash_algos,
                    default="sha256",
                    help="Select a hash algorithm (default sha256)")

args = parser.parse_args()


import sys

hash = hashlib.new(args.hash_algo)
input_data = sys.stdin.buffer.read()
hash.update(input_data)
print(hash.hexdigest())
