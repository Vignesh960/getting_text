Modules required for getting data like images,text

pip install PyMuPDF Pillow 
pip install fitz
pip install pypdf2

refer the document for data cleaning:
https://www.analyticsvidhya.com/blog/2021/06/data-extraction-from-unstructured-pdfs/



https://www.dataquest.io/blog/loading-data-into-postgres/
using python we can push into db

import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'users', sep=',')

conn.commit()


pandas data frame:
https://www.geeksforgeeks.org/python-pandas-dataframe/
https://www.w3schools.com/python/pandas/pandas_dataframes.asp
https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html








upload to db from csv
https://github.com/Strata-Scratch/csv_to_db_automation.git