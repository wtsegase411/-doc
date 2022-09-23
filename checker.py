# status code checker
import re

import requests
import csv
import time

SLEEP = 0  # Time in seconds the script should wait between requests
url_list = []
url_statuscodes = []
badSyntax = []
url_statuscodes.append(["url", "status_code"])  # set the file header for output


def checkSyntax(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        return False
    else:
        return True


def getStatuscode(url):
    try:
        r = requests.head(url, verify=False, timeout=5)  # it is faster to only request the header
        return (r.status_code)

    except:
        return -1


# Url checks from file Input
# use one url per line that should be checked

with open('C:/Users/Wenge/Desktop/BBB/mn_bbb_urls_140rows.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        url_list.append(row[3])

# Loop over full list
for url in url_list:
    if checkSyntax(url):
        print(url)
        check = [url, getStatuscode(url)]
        time.sleep(SLEEP)
        url_statuscodes.append(check)
    else:
        bad = [url]
        badSyntax.append(bad)
        with open("badSyntaxWrite.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(badSyntax)

# Save file
with open("urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)
