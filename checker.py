import re
from urllib.parse import urlparse
import requests
import csv
import time

SLEEP = 0  # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
# set the file header for output
badSyntax = [["bid", "url_id", "url"]]
fixedSyntax = [["bid", "url_id", "previous_url", "fixed_url"]]
url_statuscodes300 = [["bid", "url_id", "url", "status_code"]]
url_statuscodes200 = [["bid", "url_id", "url", "status_code"]]
url_statuscodes400 = [["bid", "url_id", "url", "status_code"]]
url_statuscodesGre400 = [["bid", "url_id", "url", "status_code"]]
url_statuscodesNeg1 = [["bid", "url_id", "url", "status_code"]]

base_dir = 'C:/Users/Medhanit Asrat/PycharmProjects/BBB/'


# Checks if the syntax of the url in the database matches the general url syntax for url.
# Checks for urls that start with http and also for those that don't
def checkSyntax(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        return False
    else:
        return True


# Attempts to fix some syntax problems
def fix(url):
    if re.match('[-a-zA-Z0-9]$', url[-1]) is None:  # get rid of special characters at the end of URL's
        url = url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to '.' in URL

    domain = urlparse(url).netloc  # extracts the domain for fixing errors in the domain

    # checks if domain starts with www and if followed by '.'
    if len(domain) >= 4:
        if domain[0] == 'w' and domain[1] == 'w' and domain[2] == 'w' and domain[3] != '.':
            domain = domain.replace('www', 'www.', domain)

    domain = re.sub('(?<!\.)((?=com$)|(?=net$)|(?=org$)|(?=edu$)|(?=gov$))', '.',
                    domain)  # add '.' before top level domains if there aren't any

    if urlparse(url).scheme:
        url = urlparse(url).scheme + "://" + domain + urlparse(url).path + urlparse(url).params + urlparse(
            url).query + urlparse(url).fragment
    else:
        url = domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment

    return url

# Returns the status code that's associated with the given url
def getStatuscode(url):
    try:
        r = requests.get(url, verify=False, timeout=5)
        return (r.status_code)

    except:
        return -1


# reads for sample data
with open(base_dir + 'mn_bbb_urls_1 250 rows .csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        bid_list.append(row[1])
        urlId_list.append(row[2])
        url_list.append(row[3])

# writes to file
def writeToFile(fileName, lst):
    with open(base_dir + fileName, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)

# tries to fix url and checks the pattern again to verify whether it has been fixed or not
def verify(url, index):
    if checkSyntax(url):
        return True, url
    else:
        fixedUrl = fix(url)
        if checkSyntax(fixedUrl):
            fixed = [bid_list[index], urlId_list[index], url, fixedUrl]
            fixedSyntax.append(fixed)
            writeToFile("fixedSyntax.csv", fixedSyntax)
            return True, fixedUrl
        else:
            return False, url


# Loop over full list and stores each url in a different CSV based on their status code and validity
for i in range(1, len(url_list)):
    a, b = verify(url_list[i], i)
    if a:
        status_code = getStatuscode(b)
        time.sleep(SLEEP)
        if (status_code <= 399) and (status_code >= 300):
            check = [bid_list[i], urlId_list[i], b, status_code]
            url_statuscodes300.append(check)
            writeToFile("urls_withStatusCode300.csv", url_statuscodes300)

        elif (status_code <= 299) and (status_code >= 200):
            check = [bid_list[i], urlId_list[i], b, status_code]
            url_statuscodes200.append(check)
            writeToFile("urls_withStatusCode200.csv", url_statuscodes200)

        elif (status_code <= 499) and (status_code >= 400):
            check = [bid_list[i], urlId_list[i], b, status_code]
            url_statuscodes400.append(check)
            writeToFile("urls_withStatusCode400.csv", url_statuscodes400)

        elif status_code == -1:
            check = [bid_list[i], urlId_list[i], b, status_code]
            url_statuscodesNeg1.append(check)
            writeToFile("urls_withStatusCodeNeg1.csv", url_statuscodesNeg1)

        elif status_code > 499:
            check = [bid_list[i], urlId_list[i], b, status_code]
            url_statuscodesGre400.append(check)
            writeToFile("urls_withStatusCodeGre499.csv", url_statuscodesGre400)

    else:
        bad = [bid_list[i], urlId_list[i], b]
        badSyntax.append(bad)
        writeToFile("badSyntax.csv", badSyntax)


