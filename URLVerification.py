import SyntaxChecker
import StatusCodeChecker
import csv
import time


def opener(base_dir, fileName, bid_list, urlId_list, url_list):  # 'mn_bbb_urls_1 100 rows .csv'
    """

    :param base_dir:
    :param fileName:
    :param bid_list:
    :param urlId_list:
    :param url_list:
    :return:
    """
    with open(base_dir + fileName, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            bid_list.append(row[1])
            urlId_list.append(row[2])
            url_list.append(row[3])


def write(base_dir, filename, lst):
    """

    :param base_dir:
    :param filename:
    :param lst:
    :return:
    """
    with open(base_dir + filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)


def main():
    base_dir = 'C:/Users/Wenge/Desktop/BBB/'
    bid_list = []
    urlid_list = []
    url_list = []
    statCheck = []
    uid = []
    badSyntax = [["bid", "url_id", "url"]]
    newfile = [["bid", "url_id", "url", "status_code"]]

    filename = 'mn_bbb_urls_1 100 rows .csv'
    opener(base_dir, filename, bid_list, urlid_list, url_list)

    for i in range(0, len(url_list)):
        a, b = SyntaxChecker.verify(url_list[i])
        if a:
            statCheck.append(b)
            uid.append(i)
        else:
            bad = [bid_list[i], urlid_list[i], b]
            badSyntax.append(bad)
            write(base_dir, "badSyntax.csv", badSyntax)

    statList = StatusCodeChecker.getstat(statCheck)

    for i in range(0, len(uid)):
        newf = [bid_list[uid[i]], urlid_list[uid[i]], statCheck[i], statList[i]]
        newfile.append(newf)
        write(base_dir, "AnalyzedUrl.csv", newfile)

    print(StatusCodeChecker.getstat(url_list))


start = time.time()
main()
end = time.time()
print(end - start)
