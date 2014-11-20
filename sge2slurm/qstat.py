#!/usr/bin/env python
import argparse

def main():
    parser = argparse.ArgumentParser("QSTAT Binary")
    parser.add_argument("-u", metavar="--user_list", help="user[@host][,user[@host],...]")
    args = parser.parse_args()
