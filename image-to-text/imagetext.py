import pytesseract
import os
from PIL import Image


def convert():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open('k.jpg')
    text = pytesseract.image_to_string(img)

    for word in text.split("\n"):
        if "”—" in word:
            word = word.replace("”—", ":")

        # normalize NIK
        if "NIK" in word:
            nik_char = word.split()
            if "D" in word:
                word = word.replace("D", "0")
            if "?" in word:
                word = word.replace("?", "7")

        print(word)


convert()
