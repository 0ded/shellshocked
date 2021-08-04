#!/usr/bin/python3

import sys

value_flags = [ ]
non_value_flags = ["-h", "-help",]

help_msg = "flag    |   description \r\n" \
            "-----------------------\r\n" \
            "-h     |   show help message\r\n" \
            "--help | \r\n" \
            ""


def get_flags():
    command = sys.argv[1:]
    flags = {}
    for i in range(len(command)):
        if command[i] in value_flags:
            flags[command[i]] = command[i+1]
            i += 1
        elif command[i] in non_value_flags:
            flags[command[i]] = ""
        else:
            print("Incorrect flag")
            exit(2)
    pass


if __name__ == '__main__':
    get_flags()
else:
    print("Incorrect use")
    exit(2)
