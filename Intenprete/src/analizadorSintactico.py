import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

precedence = (
	('right','ID','CALL','BEGIN','IF','WHILE'),
	('right','PROCEDURE'),
	('right','VAR'),
	('right', 'ASSIGN'),
	('right','UPDATE'),
	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ODD'),
	('left','LPARENT','RPARENT'),
	)

def p_program(p):
	'''program : block'''
	print "program"
	#p[0] = program(p[1],"program")

def p_block1(p):
	'''block : rule'''
	print "block (rule)"
	
def p_block2(p):
	'''block : fact '''
	print "block (fact)"
	
def p_block3(p):
	'''block : block block '''
	print "block 3"
	
def p_fact(p):
	'''fact : factname LPARENT elements RPARENT DOT'''
	#p[0] = constDecl(p[2])
	print "fact"
	
def p_rule(p):
	'''rule : factname LPARENT elements RPARENT ASSIGN goal DOT'''
	#p[0] = constDecl(p[2])
	print "rule"
	
def p_goal1(p):
	'''goal : goal COMMA goal'''
	#p[0] = constDecl(p[2])
	print "goal 1"
	
def p_goal2(p):
	'''goal : goalRule'''
	#p[0] = constDecl(p[2])
	print "goal 2"
	
def p_goalrule1(p):
	'''goalRule : factname LPARENT elements RPARENT'''
	#p[0] = constDecl(p[2])
	print "goalRule 1"
	
def p_goalrule2(p):
	'''goalRule : element EQUALITY element'''
	#p[0] = constDecl(p[2])
	print "goalRule 2 (EQUALITY)"
	
def p_goalrule3(p):
	'''goalRule : element INEQUALITY element'''
	#p[0] = constDecl(p[2])
	print "goalRule 3 (INEQUALITY)"
	
def p_factname(p):
	'''factname : ID'''
	#p[0] = constDecl(p[2])
	print "factname"
	
def p_elements1(p):
	'''elements : elements COMMA elements'''
	#p[0] = constDecl(p[2])
	print "elements 1"
	
def p_elements2(p):
	'''elements : element'''
	#p[0] = constDecl(p[2])
	print "elements 2"
	
def p_element(p):
	'''element : ID'''
	#p[0] = constDecl(p[2])
	print "element"
	

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error de sintaxis ", p
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]

def test():
	directorio = os.getcwd()+'/test/'
	archivo = buscarFicheros(directorio)
	test = directorio+archivo
	fp = codecs.open(test,"r","utf-8")
	cadena = fp.read()
	fp.close()
	
	parser = yacc.yacc()
	result = parser.parse(cadena)
	
	print result






