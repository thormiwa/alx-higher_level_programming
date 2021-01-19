#!/usr/bin/python3


''' a write-file module '''


def write_file(filename="", text=""):
    ''' function that writes a text file (UTF8) and returns the number'''
    with open(filename, 'w', encoding='utf-8')as f:
        return(f.write(text))
