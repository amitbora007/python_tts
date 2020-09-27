# pip install pyttsx3
#pip install PyPDF2



import PyPDF2
import pyttsx3


book= open("absp.pdf", 'rb')
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
print(pages)


speaker = pyttsx3.init()
#for page in range(220,pages):


for page in range(220,221):
	cpage = reader.getPage(page)
	text = cpage.extractText()
	speaker.say(text)
	speaker.save_to_file(text , 'test.mp3')
	speaker.runAndWait()


# voices = speaker.getProperty('voices')
# for voice in voices:
   # speaker.setProperty('voice', voice.id)
   # text = 'The quick brown fox jumped over the lazy dog.'
   # speaker.say(text)
   # speaker.save_to_file(text, 'voice.mp3')
   # speaker.runAndWait()