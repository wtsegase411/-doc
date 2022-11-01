import pandas as pd
import random

## Provide file name with path
base_dir = 'C:/Users/Wenge/Desktop/BBB/mn_bbb_urls.csv'

pd_dataframe = pd.read_csv(base_dir, header=0)
number_of_rows = 10000 #len(pd_dataframe.index) + 1


print(f"{number_of_rows}")

## Incase of equal split, provide the same number for min and max
min_rows = 1
max_rows = 10001

file_increment = 1
skip_rows = 1

## first file random numbers
number_of_rows_perfile = 10000 #random.randint(min_rows, max_rows)

while True:

    if number_of_rows_perfile <= 0:
        break
    ## Read CSV file with number of rows and skip respective number of lines
    df = pd.read_csv(base_dir, header=None, nrows = number_of_rows_perfile,skiprows = skip_rows)

    ## Target file name
    split_target_file = f"{base_dir[:-4]}_{file_increment} 100 rows .csv"

    ## write to csv
    df.to_csv(split_target_file, index=False, header=False, mode='a', chunksize=number_of_rows_perfile)

    file_increment += 1

    skip_rows += number_of_rows_perfile

    ## Last file handler
    if skip_rows >= number_of_rows:
        number_of_rows_perfile = number_of_rows - skip_rows
    else:
        number_of_rows_perfile = random.randint(min_rows, max_rows)

