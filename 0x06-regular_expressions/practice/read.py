#!/usr/bin/python3

"""Defines a text file-reading function"""

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        regex = /[World!]/
        print(text.replace(regex "Kenya!"))
        print(f.read())


read_file("text.txt")
