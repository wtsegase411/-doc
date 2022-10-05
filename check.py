import re
from urllib.parse import urlparse

import requests

# print('hello world')
# print('contacting google.com...')
# r = requests.head("https://www.youtube.com/non-exist-url")
# print("status code:", r.status_code)
# url = 'https://www.youtube.com/non-exist-url'
# request = requests.get(url)
# print(request.status_code)
from pyparsing import Regex

url = "https://wwwfacebook,com/search/top/?q=king%20milan%20barber%20shop#"


def check(url):
    regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    #regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    # url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    # url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    if re.match(regex, url) is None:
        # print('False')
        return False
    else:
        # print('True')
        return True


def fixSyntax(url):
    url = url.lower()  # standardize to lowercase
    if (re.match('[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]$', url) == None ):
        url=url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to . in URL
    #url = re.Replace(url, "(?m)(?<=^.{len(url)-2})-"," ")
    domain = urlparse(url).netloc
    domain = re.sub('(?<!\.)((?=com$)|(?=net$)|(?=org$)|(?=edu$)|(?=gov$))', '.', domain)
    #domain = re.sub('\.om$', '.com', domain)  # replace .om with .com (if at the end)

    if (urlparse(url).scheme):
        url = urlparse(url).scheme +"://"+ domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment
    else:
        url = domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment

    print(url)
    print(domain)


if check(url):
    print("clean URl")
else:
    fixSyntax(url)
