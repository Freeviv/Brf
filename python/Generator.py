#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:52:58 2017

@author: janschon
"""

import os
import binascii

DECLARATION = "static const unsigned char"


class Generator():
    def __init__(self,m_path,m_tree):
        if not os.path.exists(os.path.abspath(m_path)):
            print("Error: \"" + os.path.abspath(m_path) + "\" does not exist")
            return
        if not m_tree:
            print("Error: tree=None")
            return
        self.path = os.path.abspath(m_path)
        self.tree = m_tree

    def generate_cpp(self):
        tmp_path = self.path
        if not tmp_path.endswith("/"):
            tmp_path = tmp_path + "/"
        print(tmp_path + "generated")
        if not os.path.isdir(tmp_path + "generated"):
            os.makedirs(tmp_path + "generated")
        for prefix in self.tree.prefix_list:
            with open(tmp_path + "generated" + "/" + prefix.name + ".cpp",'w+') as pr:
                for fi in prefix.file_list:
                    file_buffer = []
                    with open(fi.path, 'rb') as f:
                        byte = f.read(1)
                        while byte != b"":
                            tmp = "0x" + binascii.hexlify(byte)
                            if tmp.endswith("0"):
                                tmp = tmp[:-1]
                            file_buffer.append(tmp)
                            byte = f.read(1)
                    pr.write(DECLARATION + " " + fi.name + "[] = " +
                             str(file_buffer).replace('[','{').replace(']','}')
                             .replace('\'',''))
                    pr.write(";\n")
