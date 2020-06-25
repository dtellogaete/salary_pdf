#Read pdf

import pdfkit
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re


conf = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

pdfkit.from_url('https://www.youtube.com/watch?v=Ln44OpVvP-8', 
                'google.pdf', configuration = conf)




def get_text(root, pages=None):
    if not pages:
        number_pages = set()
    else:
        number_pages = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    file = open(root, 'rb')
    for page in PDFPage.get_pages(file, number_pages):
        interpreter.process_page(page)
    file.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

texto = get_text('salary.pdf')



pattern = '\n'

list_pdf = re.split(pattern, texto)

school =[]
for i in list_pdf:
    pattern_school = 'EMPLEADOR'
    if pattern_school in i:
        name = re.split(pattern_school, i)        
        name = name[1].strip(': ')              
        school.append(s_name)

school.append(list_pdf[4].strip(': '))


