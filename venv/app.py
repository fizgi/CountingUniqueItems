""" A program to count the total number of email messages
    sent by each user in a given file

    author: Fatih IZGI
    date: 12-Mar-2020
    version: python 3.8.1
"""

from typing import IO, DefaultDict
from collections import defaultdict
import re


file_name: str = "mbox.txt"
users: DefaultDict[str, int] = defaultdict(int)  # to count the total number of emails for each user

try:  # to open the file
    path: IO = open(file_name, "r")
except FileNotFoundError:
    print(f"File {file_name} is not found")
else:
    with path:  # close path after opening
        for line in path:
            if line.startswith("From:"):  # find specific lines
                try:
                    match = re.findall(r'[\w.-]+@[\w.-]+', line)  # find the email address
                    users[match[0]] += 1
                except IndexError:  # no email address found in the line
                    print("Corrupted line >>> {} <<< is omitted".format(line.strip('\n')))

    for email, count in sorted(users.items(), key=lambda item: item[1], reverse=True):
        print(email.ljust(32, "-"), count)  # print emails and the number of emails sorted by count
