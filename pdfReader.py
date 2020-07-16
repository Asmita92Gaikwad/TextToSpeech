import pyttsx3
import PyPDF2



book = open('Fluent Python.pdf','rb')

pdfRead = PyPDF2.PdfFileReader(book)
pages = pdfRead.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfRead.getPage(28)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
