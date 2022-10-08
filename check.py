import re
from urllib.parse import urlparse

url = "https://www.facebook,com/search/top/?q=king%20milan%20barber%20shop;"

def check(url):
    #regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    regex = "^https:\\/\\/(?:[w]{3}\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if re.match(regex, url) is None:
        return False
    else:
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

    #print(url)
    return url

check(url)
if check(url):
    print("clean URl")
else:
    print("Not clean URL")
    print(fixSyntax(url))




