from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import requests


def get_statuscode(lst):
    """
    :param lst:
    :return:
    """
    executor = ThreadPoolExecutor(max_workers=70)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    timeout = 5
    results = []
    for result in executor.map(status_code, lst, repeat(headers), repeat(timeout)):
        results.append(result)

    return results


def status_code(url, headers, timeout):
    """

    :param url:
    :param headers:
    :param timeout:
    :return:
    """
    try:
        r = requests.get(url, verify=True, timeout=timeout, headers=headers)
        return r.status_code

    except:
        return -1
