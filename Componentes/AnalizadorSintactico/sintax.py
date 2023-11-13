import ply.yacc as sint
from AnalizadorLexico.tokens import tokens

def p_programa(p):
  'programa : sentencias | sentencias programa'

def p_asignacion(p):
  'asignacion : LET IDENTIFIER EQ valor'

def p_valor(p):
  '''
  valor : INTEGER | FLOAT | IDENTIFIER
  
  '''
def p_sentencias(p):
  '''
  sentencias : asignacion | impresion
  '''
def p_impresion(p):
  '''
  impresion : PRINTLN LPAREN IDENTIFIER RPAREN
  
  '''

def p_funcion(p):
  '''
  funcion: FN IDENTIFICADOR LPAR RPAR LLLAVE programa RLLAVE
  
  '''

def p_error(p):
  print(f"Error sintáctico en la entrada {p}")

parser = sint.yacc()
