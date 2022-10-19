import re
from urllib.parse import urlparse
import requests
import csv
import time


SLEEP = 0  # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
badSyntax = [["bid", "url_id", "url"]]
fixedSyntax = [["bid", "url_id", "previous_url", "fixed_url"]]
url_statuscodes300 = [["bid", "url_id", "url", "status_code"]]  # set the file header for output\
url_statuscodes200 = [["bid", "url_id", "url", "status_code"]]
url_statuscodes400 = [["bid", "url_id", "url", "status_code"]]
url_statuscodesGre400 = [["bid", "url_id", "url", "status_code"]]
url_statuscodesNeg1 = [["bid", "url_id", "url", "status_code"]]
base_dir = 'C:/Users/Wenge/Desktop/BBB/'


def checkSyntax(url):

    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        urlfix = fix(url)


        return False
    else:
        return True



def fix(url):

    if re.match('[-a-zA-Z0-9]$', url[-1]) is None:  # get rid of special characters at the end of URL's
        url = url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to . in URL
    # extract the domain from the URL
    domain = urlparse(url).netloc

    #

    if len(domain) == 4:
        if domain[0] == 'w' and domain[1] == 'w' and domain[2] == 'w' and domain[3] != '.':
            domain = re.sub('www', 'www.', domain)

    domain = re.sub('(?<!\.)((?=com$)|(?=net$)|(?=org$)|(?=edu$)|(?=gov$))', '.', domain)
    # domain = re.sub('\.om$', '.com', domain)  # replace .om with .com (if at the end)

    if (urlparse(url).scheme):
        url = urlparse(url).scheme + "://" + domain + urlparse(url).path + urlparse(url).params + urlparse(
            url).query + urlparse(url).fragment
    else:
        url = domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment

    print(url)
    return url

def getStatuscode(url):
    try:
        r = requests.get(url, verify=False, timeout=5)
        return (r.status_code)

    except:
        return -1




# Url checks from file Input
# use one url per line that should be checked

with open(base_dir + 'mn_bbb_urls_1 100 rows .csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        bid_list.append(row[1])
        urlId_list.append(row[2])
        url_list.append(row[3])
    print(url_list)

def writeToFile(fileName, lst):
    with open(base_dir + fileName, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)

# Loop over full list

for i in range(1, len(url_list)):
    # print(url)
    if checkSyntax(url_list[i]):
        status_code = getStatuscode(url_list[i])
        time.sleep(SLEEP)
        if (status_code <= 399) and (status_code >= 300):
            check = [bid_list[i], urlId_list[i], url_list[i], status_code]
            url_statuscodes300.append(check)
            writeToFile("urls_withStatusCode300.csv", url_statuscodes300)

        elif (status_code <= 299) and (status_code >= 200):
            check = [bid_list[i], urlId_list[i], url_list[i], status_code]
            url_statuscodes200.append(check)
            writeToFile("urls_withStatusCode200.csv", url_statuscodes200)

        elif (status_code <= 499) and (status_code >= 400):
            check = [bid_list[i], urlId_list[i], url_list[i], status_code]
            url_statuscodes400.append(check)
            writeToFile("urls_withStatusCode400.csv", url_statuscodes400)

        elif status_code == -1:
            check = [bid_list[i], urlId_list[i], url_list[i], status_code]
            url_statuscodesNeg1.append(check)
            writeToFile("urls_withStatusCodeNeg1.csv", url_statuscodesNeg1)

        elif status_code > 499:
            check = [bid_list[i], urlId_list[i], url_list[i], status_code]
            url_statuscodesGre400.append(check)
            writeToFile("urls_withStatusCodeGre499.csv", url_statuscodesGre400)

    else:
        bad = [bid_list[i], urlId_list[i], url_list[i]]
        badSyntax.append(bad)
        writeToFile("badSyntax.csv", badSyntax)




# Save file
