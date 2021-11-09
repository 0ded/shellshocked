# created by Oded Ginat 2021
# Tested on python 3.8 and above

import os
import sys
import re


def main():
    # get_funcs("WinQuake/cd_null.c")
    filename = sys.argv[1]
    funcs = get_funcs_split(filename)
    create_h_file(filename, funcs)
    pass


def get_funcs_split(filename):
    with open(filename, "r") as file:
        file = file.readlines()
        out = ""
        for line in file:
            out += (line.replace("\n", " "))
        # print(out)
        # inb = re.split('{.*?}', file)
        inb = re.sub("//.*?$|/\*.*?\*/|{.*?}|#.*?(\".*?\"|>)", '', out, flags=re.S)
        inb = re.split('  +', inb)
    return inb


def create_h_file(filename, funcs):
    h_file = ".h".join(filename.rsplit(".c", 1))
    with open(h_file, "a") as file:
        for func in funcs:
            if(func != ""):
                file.write(func+";\n")


if __name__ == "__main__":
    main()
