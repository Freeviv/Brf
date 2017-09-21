#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:15:28 2017

@author: janschon
"""

import os.path
import xml.etree.ElementTree as ET

from FileTree import FileTree

class FileParser():
    def __init__(self, path):
        self.m_exists = os.path.isfile(path)
        self.m_path = path
        self.ft = FileTree()

    def exists(self):
        return self.m_exists
    
    def load_config(self):
        self.tree = ET.parse(self.m_path)
        self.root = self.tree.getroot()
    
    def generate_file_tree(self):
        for child in self.root:
            if(child.tag == "prefix"):
                self.ft.set_prefix(child.attrib["name"])
                for f in child:
                    if f.tag == "file":
                        ret_val = self.ft.new_file(f.attrib["path"],f.attrib["name"])
                        if ret_val == 0:
                            pass
                        elif ret_val == 1:
                            print("File \"" + f.attrib["path"] + "\" does not exist!")
                        elif ret_val == 2: # TODO fix this
                            print("Name \"" + f.attrib["name"] + "\" of file \"" + f.attrib["path"] + "\" already exists!")

    def get_tree_stats(self):
        return self.ft.get_stats()
    
    def get_file_sizes(self):
        return self.ft.calc_complete_size()
    
    def get_tree(self):
        return self.ft