# created by Oded Ginat 2021
# Tested on python 3.8 and above

import os
import sys
import re


def main():
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        inb = create_inb(filename)
        inb = remove_block(inb)
        inb = remove_commands(inb)
        inb = remove_includes(inb)
        create_h_file(filename, inb)


def get_funcs_split(filename):
    with open(filename, "r") as file:
        file = file.readlines()
        out = ""
        for line in file:
            out += (line.replace("\n", "!!"))
        # inb = re.sub("{.*?}|//.*?$|/\*.*?\*/|#.*?(\".*?\"|>)", '', out)
        inb = re.sub("/\*.*?\*/|//.*?!!", '', out)
        inb = re.sub("{.*?}", '', inb)
        inb = inb.replace("!!", "\n")
        inb = re.sub("#.*?(\".*?\"|>)", '', inb)
        # inb = inb.replace("\n", "")
        inb = re.split('  +|\n', inb)
    return inb


# removes comments + creats inb
def create_inb(filename):
    with open(filename, "r") as file:
        file = file.readlines()
        out = ""
        for line in file:
            out += (line.replace("\n", "!!"))
        inb = re.sub("/\*.*?\*/|//.*?!!", '', out)
        inb = inb.replace("!!", "\n")
    return inb


def split_functions(inb):
    pass


def remove_brackets(inb):
    inb = inb.replace("{", "")
    inb = inb.replace("}", "")
    return inb


def remove_commands(inb):
    inb = re.sub("\n.*?;", '', inb)
    inb = re.sub("(if|while|else|else if).*?\n", '', inb)
    # inb = re.sub("for.*?;.*?;.*?\)", '', inb)
    return inb


def remove_block(inb):
    get_sub = False
    count = 0
    sub = ""
    for char in inb:
        if get_sub:
            sub += char
        if char == "{":
            if count == 0:
                get_sub = True
                sub += "{"
            count += 1
        if char == "}":
            count -= 1
            if count == 0:
                inb = inb.replace(sub, "")
                sub = ""
                get_sub = False
    return inb


def remove_includes(inb):
    inb = re.sub("#.*?(\".*?\"|>|\n)", '', inb)
    return inb

def create_h_file(filename, funcs):
    h_file = ".h".join(filename.rsplit(".c", 1))
    open(h_file, 'w').close()
    with open(h_file, "a") as file:
        for func in funcs.split("\n"):
            if func:
                file.write(func +";\n")
        file.close()


if __name__ == "__main__":
    main()
