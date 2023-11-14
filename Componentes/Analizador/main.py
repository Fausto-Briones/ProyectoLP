import ply.yacc as sint
from tokens import tokens
from lexico import *


#Fausto
def p_programa(p):
  '''programa : sentencias
              | sentencias programa
  '''
#Fausto
def p_asignacion(p):
  'asignacion : LET IDENTIFIER ASIG valor'
#Fausto
def p_valor(p):
  '''
  valor : INTEGER 
          | FLOAT 
          | IDENTIFIER
  
  '''
#Fausto
def p_sentencias(p):
  '''
  sentencias : asignacion SEMICOLON
              | impresion SEMICOLON
              | funcion SEMICOLON
              | ingreso_datos SEMICOLON
              | arreglos SEMICOLON

  '''
def p_impresion(p):
  '''
  impresion : PRINTLN LPAREN valor RPAREN
  
  '''
#Axcel
def p_funcion(p):
  '''
  funcion : FN IDENTIFIER LPAREN RPAREN LLLAVE programa RLLAVE
  
  '''

#Emilio
def p_ingreso(p):
  '''
  ingreso_datos : STD DOUBLE_COLON IO DOUBLE_COLON DOT STDIN LPAREN RPAREN DOT READLINE LPAREN REFERENCE MUT IDENTIFIER RPAREN

  '''

#Axcel
def p_arreglos(p):
  '''
  arreglos : LCORCH valores RCORCH

  '''

#Axcel
def p_valores(p):
  '''
  valores: valor
          | valor COMMA valores

  '''
#Fausto
def p_error(p):
  print(f"Error sintáctico en la entrada {p}")

#Emilio
parser = sint.yacc()
while True:
   try:
       s = input('esp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)