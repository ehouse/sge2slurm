#!/usr/bin/env python
import argparse
import re

def main():
    # Argparse flag definitions
    parser = argparse.ArgumentParser()
    parser.add_argument("-A", metavar="Account_Name", type=str, help="Specify the account under which to run the job.", action='store', required=False)
    parser.add_argument("-b", choices=[' y',' n'], action="store", help="Wether the command is a binary or not. The options are y for binary and no for not.", required=False)
    parser.add_argument("-cwd", action="store_true", help="Place the output files (.e,.o) in the current working directory.", required=False)
    parser.add_argument("-N", metavar="name", action="store", type=str, help="The name of the job.", required=False)
    parser.add_argument("-m", metavar="[b|e|a|s|n]", action="store", type=str, help="Defines what conditions emails are sent.", required=False)
    parser.add_argument("-M", metavar="user[@host]", action="store", type=str, help="Users or emails to send results to.", required=False)
    parser.add_argument("-j", choices=[' y',' n'], action="store", help="Wether to merge STDOUT and STDERR.", required=False)
    parser.add_argument("-V", help="Use Environment Variables", action='store_true', required=False)
    parser.add_argument("filename", type=str, help="Script to run.")

    args = parser.parse_args()

    # load the script
    with open(args.filename, 'r') as f:
        # Remove whitespace from every line in script
        script = map(str.strip, f.readlines())

        # Grab every line starting with '#$' and store it in a new list removing all non matching lines and the first 3 characters
        sgelines = [y.string[3:] for y in [re.search('^#\$', x) for x in script] if y is not None]

    # Parse shell args and script args
    args = parser.parse_args(sgelines)

    # Map commands to squeue
