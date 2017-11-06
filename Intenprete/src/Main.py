import analizadorLexico
import analizadorSintactico
import os

if __name__ == '__main__':
    pass

i1 = raw_input('Prueba Lexica 1) \nPrueba Sintactica 2)\nOpcion: ')
print ""
if i1 == '1':
    analizadorLexico.test()

if i1 == '2':
    analizadorSintactico.test()

