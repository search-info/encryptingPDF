from PyPDF2 import PdfFileReader, PdfFileWriter
import os
#pdf encryption code inspired from: https://stackoverflow.com/questions/43475295/encrypt-pdfs-in-python

#changing the system current working directory
filename = input("Enter the file path and name for the file you want to encrypt: ")

# #encrypting pdf file
# with open(filename, "rb") as in_file:
#     input_pdf = PdfFileReader(in_file)
file = "test.pdf"
try:
    file = open(filename, "rb")
except:
    print("File not Found!")

input_pdf = PdfFileReader(file)
output_pdf = PdfFileWriter()
output_pdf.appendPagesFromReader(input_pdf)
output_pdf.encrypt("password")

with open("output.pdf", "wb") as out_file:
        output_pdf.write(out_file)