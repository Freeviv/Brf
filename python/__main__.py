#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:14:08 2017

@author: janschon
"""
import sys

from file_parser import FileParser
from Generator import Generator

def print_tree_stats(tree):
    print("Printing resource tree stats:")
    stats = tree.get_tree_stats()
    size = tree.get_file_sizes()
    print("The tree has " + str(stats["prefix"]) + " prefixes "
          "containing a total of " + str(stats["nodes"]) + " nodes.")
    print("The complete size of all files is: " + str(size) + " bytes.")
    

def main():
    fp = None
    if len(sys.argv) == 1:
        print("Usage: <command> <configuration-file>")
        return
    else:
        fp = FileParser(sys.argv[1])
    if not fp.exists():
        print("Configuartion file does not exists! Please check the given path.")
        return
    fp.load_config()
    fp.generate_file_tree()
    print_tree_stats(fp)
    gen = Generator("/home/janschon/",fp.get_tree())
    gen.generate_cpp()

if __name__ == "__main__":
    main()

