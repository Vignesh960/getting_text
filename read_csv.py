# PYthon program to read
# CSV file without csv module


import pandas as pd

def fun():
    #reading a csv file with pandas
    data_frame = pd.read_csv("./779390-566883_Tables/East_Primary_tab.csv")

    #give the datatype of a pandas
    # object
    print(type(data_frame))

    #this function gives us a
    # brief view of the data.
    print(data_frame.head)
    print("*"*40)

    #converting pandas dataframe
    # to a numpy array.

    arr = data_frame.to_numpy()
    print(arr[0])
    for i in arr:
        f=open('text.txt','a')
        f.write(str(i))
from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
import io

import csv
#read structured data
def read_csv(filename):
    mylist=[]
    with open(filename) as numbers:
        numbers_data=csv.reader(numbers,delimiter=",")
        next(numbers_data)#skips the header
        for row in numbers_data:
            mylist.append(row)
            return mylist
new_list=read_csv('csv.csv')
for row in new_list:
    print(row)













