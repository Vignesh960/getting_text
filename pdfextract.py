import os

import fitz

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

#convert pdf to image
def convert_to_img():
    file=fitz.open("mgu.pdf")
    # page=len(file)
    for page in file:
        pix=page.get_pixmap()
        pix.save("page-%i.png" % page.number)
#not working
# def getimg_text():
#     file=fitz.open("pdf.pdf")
#     for pageNumber,page in enumerate(file.pages(),start=1):
#         text=page.getText()
#         txt=open("report_page_{}.txt",'a'.format(pageNumber))
#         txt.writelines(text)
#         txt.close()



from PyPDF2 import PdfReader

def getimage():
    file_name="pdf.pdf"
    reader = PdfReader(file_name)
    for page in reader.pages:
        for image in page.images:
            with open(image.name, "wb") as fp:
                fp.write(image.data)
    print("images extrated from the {}".format(file_name))
