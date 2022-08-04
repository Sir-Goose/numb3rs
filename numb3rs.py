import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False

    i = 0
    while i < 4:
        if int(ip[i]) > 255:
            return False
        i = i + 1

    return True


if __name__ == "__main__":
    main()
