import re
import os
import docx
import csv
import unicodedata
from collections import Counter
import markovify

abspath = os.path.abspath(__file__)
directorio_script = os.path.dirname(abspath)
os.chdir(directorio_script)
text_a = open("Divina_Commedia.txt").read()
generator_a = markovify.Text(text_a)
length = 60
intentos = "tries = 100"
def poema():
    for i in range(10):
        print(generator_a.make_short_sentence(length, tries=100))
    i = input("""¿otro? ["si"]""")
    if i.lower == "si" or "sí":
        poema()

poema()