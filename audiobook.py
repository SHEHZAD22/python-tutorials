import pyttsx3
import PyPDF2
book=open('DBMS ASSIGNMENT.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
# pages=pdfReader.numPages
# print(pages)
speaker=pyttsx3.init()
page=pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
# speaker.say('hey this is shehzad. studying in starex university')
speaker.runAndWait()