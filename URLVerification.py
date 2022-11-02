import SyntaxChecker
import StatusCodeChecker
import csv
import time


def opener(base_dir, file_name, bId_list, urlId_list, url_list):  # 'mn_bbb_urls_1 100 rows .csv'
    """
    opens a csv file
    :param base_dir:
    :param file_name:
    :param bId_list:
    :param urlId_list:
    :param url_list:
    :return:
    """
    with open(base_dir + file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            bId_list.append(row[1])
            urlId_list.append(row[2])
            url_list.append(row[3])


def write(base_dir, file_name, lst):
    """
    writes to the csv file
    :param base_dir:
    :param file_name:
    :param lst:
    :return:
    """
    with open(base_dir + file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)


def main():
    base_dir = 'C:/Users/Medhanit Asrat/PycharmProjects/BBB/'
    bId_list = []  # sonarlint suggests b_id_list
    urlId_list = []
    url_list = []
    status_check = []
    uid = []
    bad_syntax = [["bid", "url_id", "url"]]
    new_file = [["bid", "url_id", "url", "status_code"]]

    file_name = 'mn_bbb_urls_1 250 rows .csv'
    opener(base_dir, file_name, bId_list, urlId_list, url_list)

    for i in range(len(url_list)):
        is_valid, url = SyntaxChecker.verify(url_list[i])
        if is_valid:
            status_check.append(url)
            uid.append(i)
        else:
            bad = [bId_list[i], urlId_list[i], url]
            bad_syntax.append(bad)
            write(base_dir, "bad syntax.csv", bad_syntax)

    status_list = StatusCodeChecker.get_statuscode(status_check)

    for i in range(len(uid)):
        new_f = [bId_list[uid[i]], urlId_list[uid[i]], status_check[i], status_list[i]]
        new_file.append(new_f)
        write(base_dir, "Analyzed Url.csv", new_file)

    print(StatusCodeChecker.get_statuscode(url_list))


start = time.time()
main()
end = time.time()
print(end - start)
