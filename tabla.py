import tabula as tb
#extracting the pdf to csv
def tab():
    pdf_path="pdf.pdf"
    dfs=tb.read_pdf(pdf_path,pages="all")
    print(dfs)
    #dfs[0].to_csv("first.csv")
    #tb.convert_into(pdf_path,"first.csv",output_format="csv",pages="1")
    d = tb.convert_into("pdf.pdf", "output.csv", output_format="csv", pages='all')



tab()
# file = 'pdf.pdf'
# df = tb.read_pdf(file, lattice=True, pages='all')
# d=tb.convert_into("pdf.pdf", "output.csv", output_format="csv", pages='all')
#
