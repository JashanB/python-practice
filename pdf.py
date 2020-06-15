import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
pdfFileObject = open("eg.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
pageObject = pdfReader.getPage(0)
text = pageObject.extractText()
file1 = open("/Users/JD/lighthouse/python/example.txt")
file1.writelines(text)
file1.close