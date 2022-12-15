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
file=fitz.open("mgu.pdf")
# page=len(file)
for page in file:
    pix=page.get_pixmap()
    pix.save("page-%i.png" % page.number)

    

