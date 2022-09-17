import pandas
base_dir = 'C:/Users/Wen Sun/PycharmProjects/BBB/'
csvFile = pandas.read_csv(base_dir+'mn_bbb_urls.csv',nrows=10)['URL']
print(csvFile)