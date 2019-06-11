#!/usr/bin/env python
# hash.py
#
# Takes raw text from STDIN, prints hashed data to STDOUT. Defaults to sha-256.

import argparse
import hashlib


hash_algos = hashlib.algorithms_available

parser = argparse.ArgumentParser(description="Hash raw text data from STDIN.")

parser.add_argument("-l", "--list",
                    default=False,
                    action="store_true",
                    help="List all available algorithms")

for algorithm in hash_algos:
    parser.add_argument("--{}".format(algorithm),
                        dest="hash_algo",
                        default="sha256",
                        action="store_const",
                        const=algorithm,
                        help="Select a hash algorithm (default sha256)")

args = parser.parse_args()


if args.list:
    for algorithm in hash_algos:
        print(algorithm)
else:
    import sys

    hash = hashlib.new(args.hash_algo)
    input_data = sys.stdin.buffer.read()
    hash.update(input_data)
    print(hash.hexdigest())
