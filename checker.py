# status code checker
import requests
import csv
import time

SLEEP = 0 # Time in seconds the script should wait between requests
bid_list = []
urlId_list = []
url_list = []
url_statuscodes300 = [["bid","url_id","url","status_code"]] # set the file header for output\
url_statuscodes200 = [["bid","url_id","url","status_code"]]
url_statuscodes400 = [["bid","url_id","url","status_code"]]
url_statuscodesGre400 = [["bid","url_id","url","status_code"]]
url_statuscodesNeg1 = [["bid","url_id","url","status_code"]]
base_dir = 'C:/Users/Wen Sun/PycharmProjects/BBB/'

def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)

    except:
        return -1


# Url checks from file Input
# use one url per line that should be checked
with open('C:/Users/Wen Sun/PycharmProjects/BBB/mn_bbb_urls_1 40 rows .csv', newline='') as f:

    reader = csv.reader(f)
    for row in reader:
        bid_list.append(row[1])
        urlId_list.append(row[2])
        url_list.append(row[3])
    print(url_list)

# Loop over full list

for i in range(1, len(url_list)):
    #print(url)

    status_code = getStatuscode(url_list[i])
    time.sleep(SLEEP)
    if (status_code <= 399) and (status_code >= 300):
        check = [bid_list[i], urlId_list[i], url_list[i],status_code]
        url_statuscodes300.append(check)
        with open(base_dir + "urls_withStatusCode300.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(url_statuscodes300)

    elif (status_code <= 299) and (status_code >= 200):
        check = [bid_list[i], urlId_list[i], url_list[i],status_code]
        url_statuscodes200.append(check)
        with open(base_dir + "urls_withStatusCode200.csv", "w", newline="") as f1:
            writer = csv.writer(f1)
            writer.writerows(url_statuscodes200)

    elif (status_code <= 499) and (status_code >= 400):
        check = [bid_list[i], urlId_list[i], url_list[i],status_code]
        url_statuscodes400.append(check)
        with open(base_dir + "urls_withStatusCode400.csv", "w", newline="") as f2:
            writer = csv.writer(f2)
            writer.writerows(url_statuscodes400)

    elif status_code == -1:
        check = [bid_list[i], urlId_list[i], url_list[i], status_code]
        url_statuscodesNeg1.append(check)
        with open(base_dir + "urls_withStatusCodeNeg1.csv", "w", newline="") as f3:
            writer = csv.writer(f3)
            writer.writerows(url_statuscodesNeg1)

    elif status_code > 499:
        check = [bid_list[i], urlId_list[i], url_list[i], status_code]
        url_statuscodesGre400.append(check)
        with open(base_dir + "urls_withStatusCodeGre499.csv", "w", newline="") as f4:
            writer = csv.writer(f4)
            writer.writerows(url_statuscodesGre400)



# Save file
