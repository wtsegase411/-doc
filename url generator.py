import requests
import pandas as pd
import tldextract as tldextract
from googlesearch import search
import time

companyName = "Lewk"


# address = "775 40th Ave"
# State = "MN"
# city = "Beaver Creek"
# email = "midwestcanine@earthlink.net"


def getURL(companyName):

    """
    Return company's URL given company name and state
        :param companyName: the name of the company
        :param State: the state where the company located
        :return:
            company's URL if found, else return ''
    """
    correctUrl = ''
    try:

        # term = "Lewk hr@lewk.com 945 Broadway ST NE #160 Minneapolis MN"

        term = ' '.join([companyName])

        for j in search(term, num=20, stop=20, pause=2):
            print(j)
            if pickUrl(companyName,j):
                return j

    except:
        return ''

def pickUrl(companyName,url):
    companyName = companyName.split(',')[0]
    companyName = companyName.lower()
    companyName = companyName.replace(" ", "")
    sub = tldextract.extract(url)
    print("Subdomain ", sub.domain)
    if companyName == sub.domain.lower():
        return True
    else:
        return False

print("correct Url:-->", getURL(companyName))
