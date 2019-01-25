#-*- coding: utf-8 -*-

from docx import Document

document = Document()

paragraph = document.add_paragraph('Blah-blalallalala-alala-a-la')

document.save('test.docx')
