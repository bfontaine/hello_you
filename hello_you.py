# -*- coding: UTF-8 -*-

import re
import sys
import argparse
import subprocess

import requests


def find_ip(text):
    """
    Find the first IP in a piece of text.
    """
    for match in re.finditer(r"(?:[12]?\d{1,2}\.){3}[12]?\d{1,2}", text):
        return match


def get_city(ip):
    """
    Hit ipinfo.io to get the approximate city of a given IP.
    The function returns ``None`` if no city can be found.
    """
    r = requests.get("https://ipinfo.io/%s/geo" % ip)
    if not r.ok:
        return

    info = r.json()
    if "city" not in info:
        return

    return info["city"]


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--say", action="store_true",
            help="Use macOS's `say` to say hello to bots")
    opts = parser.parse_args()

    for line in sys.stdin:
        ip = find_ip(line)
        city = get_city(ip)
        if not city:
            continue

        text = "Hello from %s!" % city

        if opts.say:
            subprocess.call(["say", text])
        else:
            print(text, end="\r\n")


if __name__ == "__main__":
    main()
