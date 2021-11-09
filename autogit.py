#!/usr/bin/python3

import sys

value_flags = ["-f"]
non_value_flags = ["-h", "-help", ]

help_msg = "flag    |   description \r\n" \
           "-----------------------\r\n" \
           "-h      |   show help message\r\n" \
           "--help  |   \r\n" \
           ""


def get_flags():
    command = sys.argv[1:]
    flags = {}
    for i in range(len(command)):
        if command[i] in value_flags and i + 1 < len(command):
            flags[command[i]] = command[i + 1]
        elif command[i] in non_value_flags:
            flags[command[i]] = ""
        else:
            if command[i - 1] not in value_flags:
                print("Incorrect flag " + command[i])
                exit(2)
            if command[i] not in value_flags and command[i] not in value_flags:
                print("Incorrect flag " + command[i])
                exit(2)
    return flags
    pass


def show_help():
    print(help_msg)
    exit(0)


if __name__ == '__main__':
    flags = get_flags()
    for flag in flags:
        if flag == "-h" or flag == "-help":
            show_help()

else:
    print("Incorrect use")
    exit(2)
