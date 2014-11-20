#!/usr/bin/env python
import argparse
import re

def main():
    # Argparse flag definitions
    parser = argparse.ArgumentParser()
    parser.add_argument("-V", help="Use Environment Variables", action='store_true', required=False)
    parser.add_argument("-b", type=str, choices=['y','n'], action="store", help="Wether the command is a binary or not. The options are y for binary and no for not.", required=False)
    parser.add_argument("-N", metavar="name", action="store", type=str, help="Name of the job.", required=False)
    parser.add_argument("filename", type=str, help="File to run.")

    args = parser.parse_args()

    # load the script
    with open(args.filename, 'r') as f:
        script = map(str.strip, f.readlines())
        sgelines = [y.string for y in [re.search('^#\$', x) for x in script] if y is not None]
        print(sgelines)

    # Set argparse flags

    # Map commands to squeue
