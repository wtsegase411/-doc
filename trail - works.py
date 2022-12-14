
import pandas as pd
import random

## Provide file name with path for example: "C:\Users\xxxxx\flights.csv"
#split_source_file = input("File Name with absolute Path? : ")

## find number of lines using Pandas
base_dir = 'C:/Users/Medhanit Asrat/PycharmProjects/BBB/mn_bbb_urls.csv'

pd_dataframe = pd.read_csv(base_dir, header=0)
number_of_rows = 40 #len(pd_dataframe.index) + 1

## find number of lines using traditional python
# fh = open(split_source_file, 'r')
# for count, line in enumerate(fh):
#     pass
# py_number_of_rows = count

print(f"{number_of_rows}")

## Incase of equal split, provide the same number for min and max
min_rows = 1
max_rows = 41

file_increment = 1
skip_rows = 1

## first file random numbers
number_of_rows_perfile = 40 #random.randint(min_rows, max_rows)

while True:

    if number_of_rows_perfile <= 0:
        break
    ## Read CSV file with number of rows and skip respective number of lines
    df = pd.read_csv(base_dir, header=None, nrows = number_of_rows_perfile,skiprows = skip_rows)

    ## Target file name
    split_target_file = f"{base_dir[:-4]}_{file_increment} 40 rows .csv"

    ## write to csv
    df.to_csv(split_target_file, index=False, header=False, mode='a', chunksize=number_of_rows_perfile)

    file_increment += 1

    skip_rows += number_of_rows_perfile

    ## Last file handler
    if skip_rows >= number_of_rows:
        number_of_rows_perfile = number_of_rows - skip_rows
    else:
        number_of_rows_perfile = 40#random.randint(min_rows, max_rows)

