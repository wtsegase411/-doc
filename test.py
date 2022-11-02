import time
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

import requests


def getstat(lst):
    executor = ThreadPoolExecutor(max_workers=40)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    timeout = 5
    results = []
    for result in executor.map(getStatuscode, lst, repeat(headers), repeat(timeout)):
        results.append(result)

    return results


lst = ['http://thefiledepot.com',
       'http://www.ronsautorepairmankato.com',
       'http://www.abcbookwerks.com',
       'http://www.caliberproductsinc.com',
       'http://www.shackslaw.com/',
       'http://www.np-cpa.com',
       'http://creativeapestudios.com',
       'http://martinizing.com/xerxes/default.aspx',
       'http://www.linkconsultinggroup.com/',
       'https://www.igtrestore.com/',
       'http://www.ccsconcrete.com/index.html',
       'http://festlerlandsurveying.com/',
       'http://aspengarage.com',
       'http://www.AspenGarage.com',
       'https://www.aspendental.com',
       'http://www.mnintegrity.com',
       'http://www.eyeofthetigerdefense.com/',
       'http://theramg.com/',
       'http://www.freshthyme.com',
       'https://www.hsdoorsystems.com/',
       'http://www.thewhimsyfactory.com',
       'http://scottschultz.results.net/site/index.php',
       'http://www.doughertywealth.com/',
       'https://www.facebook.com/search/top/?q=king%20milan%20barber%20shop',
       'http://twigthefairy.myshopify.com/',
       'http://www.alliedartworks.com/home.html',
       'http://arcforcewelding.energy/',
       'http://www.weatheredwoodmn.com/',
       'https://signaturewoods.co/',
       'http://amigosenvironmental.com',
       'http://www.traveloview.com/',
       'http://www.synergysoftwaresolutions.com/',
       'http://www.teschservice.net/',
       'http://www.facebook.com/northstarconcretestone',
       'https://www.aigc-techsolutions.com',
       'http://www.hardmoneywebsite.com/whfinancecompany',
       'http://Vossplumbing.com',
       'http://buildupconstructionservices.com/',
       'http://www.mylegacymn.com']


# def getStatuscode(url):
#     try:
#         r = requests.get(url, verify=False, timeout=5)
#         return (r.status_code)
#
#     except:
#         return -1
# headers = {
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#          }
def getStatuscode(url, headers, timeout):
    try:
        r = requests.get(url, verify=True, timeout=timeout, headers=headers)
        return r.status_code

    except:
        return -1


start = time.time()
# for i in lst:
#     print(getStatuscode(i))
print(getstat(lst))
end = time.time()

print(end-start)


