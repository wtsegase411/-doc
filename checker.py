# status code checker
import requests
import csv
import time

SLEEP = 0 # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
url_statuscodes = []
url_statuscodes.append(["bid","url_id","url","status_code"]) # set the file header for output

base_dir = 'C:/Users/Wen Sun/PycharmProjects/BBB/'

def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)

    except:
        return -1


# Url checks from file Input
# use one url per line that should be checked
with open(base_dir+'mn_bbb_urls_1 40 rows.csv', newline='') as f:

    reader = csv.reader(f)
    for row in reader:
        bid_list.append(row[1])
        urlId_list.append(row[2])
        url_list.append(row[3])
    print(url_list)

# Loop over full list

for i in range(1, len(url_list)):
    #print(url)
    check = [bid_list[i],urlId_list[i],url_list[i],getStatuscode(url_list[i])]
    time.sleep(SLEEP)
    url_statuscodes.append(check)
print(url_statuscodes)

# Save file
with open(base_dir+"urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)