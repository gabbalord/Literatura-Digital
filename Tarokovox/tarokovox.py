import os, time, random, sys
from random import randint
from collections import Counter
import markovify

# x() splits a string into a list c() is just random. choice()
# f() picks a fresh value from a list p() prints a line and pauses
# p(s) prints strings and then waits for 2 seconds (time.sleep)
# v(t) returns random verses from text on the t file opened (must be a txt file)

ruta_completa = os.getcwd()
os.chdir(ruta_completa)

def x(s): return s.split(',')

def c(l): return random.choice(l)

def p(s=''):
    print(s.capitalize())
    sys.stdout.flush()
    time.sleep(1.3)

#definimos algunos parámetros necesarios para la función v(t)
text_a = open("programa.txt").read()
length = 60
intentos = "tries = 100"
def v(t):
    generator_a = markovify.Text(text_a)
    verso = generator_a.make_short_sentence(length, tries=100)
    return verso
    for i in range(10):
        print(generator_a.make_short_sentence(length, tries=100))
    i = input("""¿otro? ["si"]""")
    if i.lower == "si" or "sí":
        poema()

#Definimos algunos valores textuales base para el loop:
imp = "Tenemos que,Necesitamos,Es necesario,Se requiere,Hay que,Resulta obligatorio,Es imprescindible,Convendría,Sería conveniente,Es preciso"
transitivo = " defender, proteger, resguardar, amparar, salvaguardar, custodiar, velar, cuidar, respaldar, apoyar, sostener, alentar, motivar, avivar, provocar, incitar, castigar, penalizar, sancionar, disciplinar, reprender, corregir, restringir, reprimir, condenar"
sust = " los jóvenes, la juventud, la mocedad, los adolescentes, los chicos, los muchachos, el rinoceronte, el gorila, el oso polar, el elefante, el león, el panda, el lobo ibérico, el jaguar, el orangután"
lugar = " de Madrid, de Sevilla, de Granada, de Toledo, de Salamanca, de Córdoba, de Zaragoza, de Santiago de Compostela, de Cádiz, de Segovia"
while True:
    statement = v(text_a)
    if randint(1,20) % 2:
        vf = c(x(imp)) + c(x(transitivo)) + c(x(sust)) + c(x(lugar)) + ": " + statement
    else:
        vf = c(x(imp)) + c(x(transitivo)) + c(x(sust)) + ": " + statement
    p(vf)