import re
import pandas as pd
import pdfplumber
from tabulate import tabulate
def pdfcdata():
    title_list=[]
    with pdfplumber.open("pdf.pdf") as pdf:
        first_page = pdf.pages[0]
        text=first_page.extract_text()
        first_page.extract_table()
        #printing all the data
        print(text)
        #print(first_page.extract_table())

        for row in text.split('\n'):

            if row.startswith("Grid Number"):
                grid_no=row.split()[-1]
                title_list.append(row.split()[-1])

                #print(grid_no)
                #work order
            if(row.startswith("Work Order")):
                #print(row.split()[-1])
                title_list.append(row.split()[-1])
                print(title_list)
            if (row.startswith("Item")):
                #prints in table header format
                print(tabulate("",headers=["Manhole_ID"]+row.split()[0:-1]))
                #print(row.split()[0:-1])
                for i in title_list:
                    print(i,end=" ")


pdfcdata()