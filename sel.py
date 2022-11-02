import urllib

import requests
from bs4 import BeautifulSoup

# target url
url = 'http://officenters.com/'

companyName = "Officenters Minnetonka"
city = 'Minneapolis'
street = '5775 Wayzata Blvd Ste 700'
state = 'MN'
phoneNum = '9529433900'

# # making requests instance
# reqs = requests.get(url)
#
# # using the BeautifulSoup module
# soup = BeautifulSoup(reqs.text, 'html.parser')
#
# # displaying the title
# print("Title of the website is : ")
# for title in soup.find_all('location'):
#     print(title.get_text())
# lst=soup.find_all(text = True)
#
# print(lst)


# print(soup.prettify())
def scrap(url,companyName, city,street, state, phoneNum):

    count = 0
    words = [companyName, city,street, state, phoneNum]
    site = urllib.request.urlopen(url).read().decode("utf-8")
    for word in words:
        if word in site:
            print(word)
            count += 1
        else:
            print(word, "not found")
    if count == 3:
        return True

print (scrap(url,companyName,city,street, state, phoneNum))