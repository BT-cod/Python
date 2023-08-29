#import Section
from PyPDF2 import PdfWriter, PdfReader

#User Input Section
num = int(input("Enter page number you want combine from multiple documents "))

#Defining variables and pdf files Section
pdf1 = open('one.pdf', 'rb')
pdf2 = open('two.pdf', 'rb')

# Combine function for pdf files Section
pdf_writer = PdfWriter()

pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)

pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)

# Creating a new output file Section
with open('output.pdf', 'wb') as output:
        pdf_writer.write(output)
