import pyttsx3
import PyPDF2
book = open('python_tutorial.pdf', 'rb')
speaker = pyttsx3.init()
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(14)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
