# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:59:33 2021

@author: GrandLoup
"""

import nltk
import pandas as pd
import PyPDF2 as PDF2

#### import and process pdf file 
file1 = open("SPC_Louis_Range_OPORD.pdf", "rb")


reader = PDF2.PdfFileReader(file1) # reader

# import file 1-by-1
pp1 = reader.getPage(0).extractText()
pp2 = reader.getPage(1).extractText()
pp3 = reader.getPage(2).extractText()
pp4 = reader.getPage(3).extractText()

# read multiple pages iteratively
# pages = []
# for i in range(reader.getNumPages()):
#     pages[i] = reader.getPage(i).extractText()
#     print(reader.getPage(i).extractText())
    
def pdf_to_text(pdf_file):
    file_content = []
    # import pdf file, extract text and pass into a .txt
    pdf_reader = PDF2.PdfFileReader(pdf_file)
    
    # get page and content
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        p_content = page.extractText().replace("\n", "")
        file_content.append(p_content)
        



pdf_to_text("SPC_Louis_Range_OPORD.pdf")
