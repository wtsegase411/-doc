import requests
import pandas as pd
import tldextract as tldextract
from googlesearch import search
import time

companyName = "Lewk"
companyName = companyName.lower()
address = "945 Broadway ST NE #160"
State = "MN"
city = "Minneapolis"
email = "hr@lewk.com"


def getURL(companyName,email, address, city, State):

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

        term = ' '.join([companyName,email, address, city, State])

        for j in search(term, tld="co.in", num=10, stop=10, pause=2):
            print(j)
            if pickUrl(j):
                return j

    except:
        return ''

def pickUrl(url):
    sub = tldextract.extract(url)
    print("Subdomain ", sub.domain)
    if companyName == sub.domain.lower():
        return True
    else:
        return False

print("correct Url:-->", getURL(companyName,email, address, city, State))
