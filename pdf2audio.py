#This program converts a pdf file to audio file in mp3 format.

from pypdf import PdfReader
from gtts import gTTS #Google TEXT TO SPEECH LIBRARY

with open('/Users/suraj/Downloads/Invictus by William Ernest Henley.pdf', 'rb') as file:

    pdf_reader = PdfReader(file)
    number_of_pages = len(pdf_reader.pages)
    text = ' '

    for page in range(number_of_pages):

        text += pdf_reader.pages[page].extract_text()
        tts =(gTTS(text))

        tts.save('theextracted_audio.mp3')