# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:47:41 2020

@author: krizh
"""

import zipfile
z = zipfile.ZipFile("New Mills Menu w.c. 29.07.2019.docx")

z

import xml.etree.ElementTree as ET
root = ET.parse(z).getroot()
print(root)