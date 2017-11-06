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
	'''block : grules '''
	print "block 3"

def p_block4(p):
	'''block : block block '''
	print "block 4"
	
def p_grules1(p):
	'''grules : assing property directive DOT'''
	#p[0] = constDecl(p[2])
	print "grules 1"
	
def p_assing1(p):
	'''assing : ASSIGN'''
	#p[0] = constDecl(p[2])
	print "assing 1"
	
def p_assing2(p):
	'''assing : IS'''
	#p[0] = constDecl(p[2])
	print "assing 2"
	
def p_directive1(p):
	'''directive : factname DIVIDE NUMBER'''
	#p[0] = constDecl(p[2])
	print "directive 1"
	
def p_directive2(p):
	'''directive : directive COMMA directive'''
	#p[0] = constDecl(p[2])
	print "directive 2"
	
def p_property1(p):
	'''property : DYNAMIC'''
	#p[0] = constDecl(p[2])
	print "property DYNAMIC"

def p_property2(p):
	'''property : PUBLIC'''
	#p[0] = constDecl(p[2])
	print "property PUBLIC"
	
def p_property3(p):
	'''property : MULTIFILE'''
	#p[0] = constDecl(p[2])
	print "property MULTIFILE"
	
def p_property4(p):
	'''property : DISCONTIGUOUS'''
	#p[0] = constDecl(p[2])
	print "property DISCONTIGUOUS"
	
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
	print "goalRule 2 (EQUALITY)"
	
def p_goalrule3(p):
	'''goalRule : element INEQUALITY element'''
	print "goalRule 3 (INEQUALITY)"
	
def p_goalrule4(p):
	'''goalRule : element check element'''
	print "goalRule 4 (check)"
	
def p_goalrule5(p):
	'''goalRule : element assing goalRule'''
	print "goalRule 5 (assing)"
	
def p_goalrule6(p):
	'''goalRule : element operator element'''
	print "goalRule 6 (operator)"
	
def p_operator1(p):
	'''operator : MINUS'''
	print "operator MINUS"
	
def p_operator2(p):
	'''operator : PLUS'''
	print "operator PLUS"
	
def p_operator3(p):
	'''operator : TIMES'''
	print "operator TIMES"

def p_operator4(p):
	'''operator : DIVIDE'''
	print "operator DIVIDE"
	
def p_check1(p):
	'''check : GTE'''
	print "check 1"
	
def p_check2(p):
	'''check : LT'''
	print "check 2"
	
def p_check3(p):
	'''check : GT'''
	print "check 3"
	
def p_factname1(p):
	'''factname : ID'''
	print "factname ID"
	

	
def p_elements1(p):
	'''elements : elements COMMA elements'''
	#p[0] = constDecl(p[2])
	print "elements 1"
	
def p_elements2(p):
	'''elements : element'''
	#p[0] = constDecl(p[2])
	print "elements 2"
	
def p_element1(p):
	'''element : ID'''
	#p[0] = constDecl(p[2])
	print "element ID"
	
def p_element2(p):
	'''element : NUMBER'''
	print "element NUMBER"

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
	print "archivos de prueba:"
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






