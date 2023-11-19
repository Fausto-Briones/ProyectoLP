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
def p_comparacion(p):
  '''
  comparacion: IDENTIFIER LEQ IDENTIFIER
                | IDENTIFIER GEQ IDENTIFIER
                | IDENTIFIER EQ IDENTIFIER
                | IDENTIFIER NEQ IDENTIFIER
                | IDENTIFIER RIGHTARROW IDENTIFIER
                | IDENTIFIER LEFTARROW IDENTIFIER
                | IDENTIFIER EQ valor
                | IDENTIFIER NEQ valor
                | IDENTIFIER GEQ valor
                | IDENTIFIER LEQ valor
                | IDENTIFIER RIGHTARROW valor
                | IDENTIFIER LEFTARROW valor
                | valor EQ IDENTIFIER
                | valor NEQ IDENTIFIER
                | valor GEQ IDENTIFIER
                | valor LEQ IDENTIFIER
                | valor RIGHTARROW IDENTIFIER
                | valor LEFTARROW IDENTIFIER
  '''
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
#Fausto
def p_conector(p):
  '''
  conector : AND | OR
  '''
#Fausto
def p_proposicionC(p):
  '''
  proposicion: comparacion conector proposicion | comparacion
  '''
#Fausto
def p_condicional(p):
  '''
  condicional : IF comparacion LLLAVE programa RLLAVE 
                | IF proposicion LLLAVE programa RLLAVE
  '''


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
