# status code checker
import re

import requests
import csv
import time

SLEEP = 0  # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
badSyntax = [["bid", "url_id", "url"]]
# url_statuscodes300 = [["bid", "url_id", "url", "status_code"]]  # set the file header for output\
# url_statuscodes200 = [["bid", "url_id", "url", "status_code"]]
# url_statuscodes400 = [["bid", "url_id", "url", "status_code"]]
# url_statuscodesGre400 = [["bid", "url_id", "url", "status_code"]]
# url_statuscodesNeg1 = [["bid", "url_id", "url", "status_code"]]
base_dir = 'C:/Users/Medhanit Asrat/PycharmProjects/BBB/'


def getStatuscode(url):
    try:
        r = requests.get(url, verify=False, timeout=5)  # it is faster to only request the header
        return r.status_code

    except:
        return -1


def checkSyntax(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        return False
    else:
        return True


# write to file
def writeToFile(fileName):
    with open(base_dir + fileName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(fileName)


writeToFile("urls_withStatusCode300.csv")

#
# for i in range(1, len(url_list)):
#     # print(url)
#     if checkSyntax(url_list[i]):
#         status_code = getStatuscode(url_list[i])
#         time.sleep(SLEEP)
#         if (status_code <= 399) and (status_code >= 300):
#             check = [bid_list[i], urlId_list[i], url_list[i], status_code]
#             # url_statuscodes300.append(check)
#             writeToFile("urls_withStatusCode300.csv")
