from tkinter.filedialog import *
import PyPDF2
from gtts import gTTS

book = askopenfilename()
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
for page in range(0, pages):
    cur_page = reader.getPage(page)
    mytext = cur_page.extractText()
    #print(mytext)
    audio = gTTS(text = mytext, lang = 'en', slow = False)
    audio.save('try.mp3')
os.system('try.mp3')
