# import pandas
# import csv
# base_dir = 'C:/Users/Wen Sun/PycharmProjects/BBB/'
# url_list=[]
# url_dic = {}
# with open(base_dir+'test.csv', newline='') as f:
#
#     reader = csv.reader(f)
#     for row in reader:
#         url_list.append(row[3])
#     print(url_list)
# with open(base_dir+"urls_trunch.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(url_list)
import re
url = 'http://rehmins,com;'
print(url[-1])

if (re.match('[a-zA-Z0-9]',url[-1])):
    print("True")
else:
    url = url[:-1]
