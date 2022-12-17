import os


# import fitz

# file="mgu.pdf"
# pdf=fitz.open(file)
# image_list=pdf.load_page(0)
# for image in image_list:
#     xref=image[0]
#     pix=fitz.Pixmap(pdf,xref)
#     if(pix.n<5):
#        pix.writePNG(f'{xref}.png')
#     else:
#         pix1=fitz.open(fitz.csRGB,pix)
#         pix1.writePNG(f'{xref}.png')
#     pix=None
# print(len(image_list),'detected')

# convert pdf to image
def convert_pdf_to_img():
    file = fitz.open("mgu.pdf")
    # page=len(file)
    for page in file:
        pix = page.get_pixmap()
        pix.save("page-%i.png" % page.number)


# not working
# def getimg_text():
#     file=fitz.open("pdf.pdf")
#     for pageNumber,page in enumerate(file.pages(),start=1):
#         text=page.getText()
#         txt=open("report_page_{}.txt",'a'.format(pageNumber))
#         txt.writelines(text)
#         txt.close()


from PyPDF2 import PdfReader, PdfFileReader


def getimage():
    file_name = "pdf.pdf"
    reader = PdfReader(file_name)
    for page in reader.pages:
        for image in page.images:
            with open(image.name, "wb") as fp:
                fp.write(image.data)
    print("images extrated from the {}".format(file_name))


import camelot

from pdfminer.high_level import extract_text
def read_data():
    file_name = "pdf.pdf"


pdfObject = open("pdf.pdf", 'rb')

# creating a pdf reader object
pdfReader = PdfFileReader(pdfObject)

# Extract and concatenate each page's content
text = ''
for i in range(0, pdfReader.numPages):
    # creating a page object
    pageObject = pdfReader.getPage(i)
    # extracting text from page
    text += pageObject.extractText()
    f=open('text.txt','a')
    f.write(text)
print(text)

import pandas as pd
def notepad_csv():


    # readinag given csv file
    # and creating dataframe
    dataframe1 = pd.read_csv("text.txt")

    # storing this dataframe in a csv file
    dataframe1.to_csv('GeeksforGeeks.csv',index=None)
notepad_csv()