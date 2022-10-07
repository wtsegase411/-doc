import re
from urllib.parse import urlparse

url = "https://wwwgreenwoodnurserymncom;"
print(url)


def check(url):
    url = fix(url)
    regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if re.match(regex, url) is None:
        # print('False')
        return False
    else:
        # print('True')
        return True

def fix(url):

    if re.match('[-a-zA-Z0-9()@:%_+.~#?&/=]$', url[-1]) is None:  # get rid of special characters at the end of URL's
        url = url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to . in URL

    domain = urlparse(url).netloc

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


if check(url):

    print("clean URl")

else:
    print("not clean")
