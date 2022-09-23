# status code checker
import re

import requests
import csv
import time

SLEEP = 0 # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
url_statuscodes = []
badSyntax = []
badSyntax.append(["bid","url_id","url"]) # set the file header for output

url_statuscodes.append(["bid","url_id","url","status_code"]) # set the file header for output

base_dir = 'C:/Users/Wenge/Desktop/BBB/'

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

with open(base_dir+'mn_bbb_urls_140rows.csv', newline='') as f:

    reader = csv.reader(f)
    for row in reader:
        url_list.append(row[3])
        bid_list.append(row[1])
        urlId_list.append(row[2])
        url_list.append(row[3])
    print(url_list)

# Loop over full list
for i in range(1, len(url_list)):
    if checkSyntax(url_list[i]):
        print(url_list[i])
        check = [bid_list[i], urlId_list[i], url_list[i], getStatuscode(url_list[i])]
        time.sleep(SLEEP)
        url_statuscodes.append(check)
    else:
        bad= [bid_list[i], urlId_list[i], url_list[i]]

        badSyntax.append(bad)
        with open("badSyntaxWrite.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(badSyntax)

# Save file
with open(base_dir+"urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)