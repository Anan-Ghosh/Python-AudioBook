import pyttsx3 #import python to text sepeech
import PyPDF2  #import Python pdf reader 2


book=open('oop.pdf','rb') #rb means reading binary
reader=PyPDF2.PdfFileReader(book) 
pages=reader.numPages #get the total number of page in the pdf
print(pages)

speak=pyttsx3.init()  #intiialize the speaking

voices = speak.getProperty('voices')       #getting details of current voice
#speak.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speak.setProperty('voice', voices[1].id)


for x in range(1,pages):
    page=reader.getPage(x) # decalre the page number for speaking

    text= page.extractText() #convert into audio 


    speak.say(text)
    speak.runAndWait()
    speak.stop()