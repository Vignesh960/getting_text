import tabula
import os
def each_table_into_file():
    tables = tabula.read_pdf("example2.pdf", pages="all")
    folder_name = "tables"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    # iterate over extracted tables and export as excel individually
    for i, table in enumerate(tables, start=1):
        table.to_csv(os.path.join(folder_name, f"table_{i}.csv"), index=False)

import camelot
def cmaelot_pdf():
    
    #tables = camelot.read_pdf("example2.pdf",pages='1-end')
    pdf_archive = camelot.read_pdf("example2.pdf", pages="all", flavor="stream")

    for page, pdf_table in enumerate(pdf_archive):           
        #print(pdf_archive[page].df.to_csv("output.csv"))
        print(pdf_archive[page].df)
cmaelot_pdf()