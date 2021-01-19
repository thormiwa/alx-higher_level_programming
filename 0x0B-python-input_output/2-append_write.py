#!/usr/bin/python3


''' a append-file module '''


def write_file(filename="", text=""):
    ''' function that appends a string at the end of text file'''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
