import requests
import pandas as pd
from googlesearch import search
import time

def getURL(companyName):
    """
    Return company's URL given company name and state
        :param companyName: the name of the company
        :param State: the state where the company located
        :return:
            company's URL if found, else return ''
    """
    lst=[]
    try:
       # term = ' '.join([companyName, State])
       # for url in search(term, num=2):
        for url in search(companyName, num=10, stop=10, pause=2):
            lst.append(url)
        return lst
    except:
        return ''


def getStatuscode(url):
    try:
        r = requests.get(url, verify=True, timeout=5)
        return (r.status_code)

    except:
        return -1

lst= getURL('able movers llc')
#print(lst)
for i in lst:
    print (i)
    print (getStatuscode(i))

# base_dir = 'C:/Users/Wen Sun/PycharmProjects/BBB/'
# df = pd.read_csv(base_dir + 'mn_bbb_urls_1 100 rows .csv')
#
# df['URL'] = ''
# for index, row in df.iterrows():
#     df.at[index, 'URL'] = getURL(row['Compan'], row['State'])
#     time.sleep(2)