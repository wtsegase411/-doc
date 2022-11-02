import re
from urllib.parse import urlparse


def check_syntax(url):
    """
    checks if the url matches with ... and returns a true/false
    :param url:
    :return:
    """
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9(" \
                  ")@:%_\\+.~#?&\\/=]*)$ "
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"    #
    # url_pattern1 is the pattern without https

    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        return False
    else:
        return True


def fix(url):
    """
    performs a possible fixed url
    :param url:
    :return: fixed url
    """
    if re.match('[-a-zA-Z0-9]$', url[-1]) is None:  # get rid of special characters at the end of URLs
        url = url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to '.' in URL

    domain = urlparse(url).netloc  # extracts the domain for fixing errors in the domain

    domain = re.sub('(?<!\.)((?=com$)|(?=net$)|(?=org$)|(?=edu$)|(?=gov$))', '.',
                    domain)  # add '.' before top level domains if there aren't any

    if urlparse(url).scheme:
        url = urlparse(url).scheme + "://" + domain + urlparse(url).path + urlparse(url).params + urlparse(
            url).query + urlparse(url).fragment
    else:
        url = domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment

    return url


def verify(url):
    """
    idk bruv - verifies the syntax of the url and returns the
    :param url:
    :return:
    """
    if check_syntax(url):
        return True, url
    else:
        fixed_url = fix(url)
        if check_syntax(fixed_url):
            return True, fixed_url
        else:
            return False, url
