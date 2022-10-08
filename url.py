import csv

import pandas

base_dir = 'C:/Users/Medhanit Asrat/PycharmProjects/BBB/'
csvFile = pandas.read_csv(base_dir + 'mn_bbb_urls.csv', nrows=10)['URL']


trunche_url = []

#print(trunche_url)
with open("url_trunche.csv", "w", newline="") as f:
    writer = csv.writer(f)
    trunche_url.append(csvFile)
    writer.writerow(trunche_url)

    for line in trunche_url:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(line)
#print(csvFile)
