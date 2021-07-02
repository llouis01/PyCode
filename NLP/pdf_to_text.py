# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:59:33 2021

@author: GrandLoup
"""

import nltk
import pandas as pd
import PyPDF2 as PDF2

# import and process pdf file 
file1 = open("SPC_Louis_Range_OPORD.pdf", "rb")
reader = PDF2.PdfFileReader(file1)

for page in reader.getNumPages:
    reader.getPage(page).extractText()
