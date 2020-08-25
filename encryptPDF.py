from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import easygui as gui
#pdf encryption code inspired from: https://stackoverflow.com/questions/43475295/encrypt-pdfs-in-python

### encryptPDF.py version = 0.0.1
### This program aims to encrypt pdf by creating a new file that is named ENCRYPTED_{filename_here}
### The user is still responsible of properly disposing the old pdf file. Recommendations is to use file shredders

###Used pyinstaller to make it an executable... command in cmd is: python -m PyInstaller [full_file_path]

def encrypt(filename, password="password"):
    output_pdf = PdfFileWriter()
    in_file = open(filename, "rb")
    input_pdf = PdfFileReader(in_file, False)
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt(password)

    full_path = filename.split('\\')

    real_filename = full_path[len(full_path) - 1]
    new_filename = "ENCRYPTED_" + real_filename

    # print(f"full path: {full_path}\n real filename: {real_filename}\n new filename: {new_filename}\n")
    # print(new_filename)

    with open(new_filename, "wb") as out_file:
        output_pdf.write(out_file)

    in_file.close()

    #gui.msgbox(f"Your file is encrypted and is named: {new_filename}, however you must properly dispose of the old unencrypted file. Recommendation is to use file shredders", 'Encryption Done!')

def main():

    file_name = gui.fileopenbox("Select a file to encrypt")
    if (file_name == None):
        sys.exit(1)

    pass_word = gui.passwordbox('Enter a password for the PDF[if left blank then default value of \'password\' will be used]', 'PDF Encryption')

    try:
        encrypt(file_name, pass_word)
    except:
        gui.msgbox('Something went wrong...', 'PDF encryption Error')
        sys.exit(1)

main()

