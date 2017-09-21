#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:35:09 2017

@author: janschon
"""

import os.path

class File():
    def __init__(self, p_path, p_name):
        self.path = p_path
        self.name = p_name
    
    def __bool__(self):
        return os.path.isfile(self.path)

class Prefix():
    def __init__(self,p_name):
        self.name = p_name
        self.file_list = []
        self.name_list = []

    def add_file(self, path, name):
        if name in self.name_list:
            return 2
        self.file_list.append(File(path,name))
        self.name_list.append(name)
        return 0
    
    def __len__(self):
        return len(self.file_list)
    
    def __contains__(self, *elem, **k):
        return self.name in elem

class FileTree():
    def __init__(self):
        self.prefix_list = []
        self.current_prefix = None

    def set_prefix(self,p_prefix):
        self.current_prefix = None
        for p in self.prefix_list:
            if p.name == p_prefix:
                self.current_prefix = p
        # given prefix not in list, creating new
        if not self.current_prefix:
            self.current_prefix = Prefix(p_prefix)
            self.prefix_list.append(self.current_prefix)
    
    def new_file(self, path, name):
        if not os.path.isfile(path):
            return 1
        return self.current_prefix.add_file(os.path.abspath(path),name)
    
    def get_stats(self):
        le = 0
        ret_val = {}
        for p in self.prefix_list:
            le = le + len(p)
        ret_val["prefix"] = len(self.prefix_list)
        ret_val["nodes"] = le
        return ret_val
    
    def calc_complete_size(self):
        size = 0
        for prefix in self.prefix_list:
            for fi in prefix.file_list:
                size = size + os.path.getsize(fi.path)
        return size