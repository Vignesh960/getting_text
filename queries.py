import mysql.connector
import MySQLdb

import csv
def csv():
    try:
        con = mysql.connector.connect(host="localhost", username='root', passwd='root', database="world")
        cur = con.cursor()
        loc = ".//779390-566883_Tables//East_Primary_tab.csv"
        with open(loc,'r') as csv_file:
            csvfile=csv.reader(csv_file,delimiter=",")
            values=[]


    except mysql.connector.DatabaseError as db:
        print("DB problem", db)

query="insert into manahole "