import ply.yacc as sint
from tokens import tokens
from lexico import *


#Fausto
def p_programa(p):
  '''programa : sentencias
              | sentencias programa
  '''
#Fausto & Emilio
def p_asignacion(p):
  '''asignacion : LET IDENTIFIER ASIG valor
                  | LET MUT IDENTIFIER ASIG valor
                  | LET IDENTIFIER COLON asig_data_type ASIG valor
                  | LET MUT IDENTIFIER COLON asig_data_type ASIG valor'''
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
#Fausto & Emilio
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
              | control_structure SEMICOLON
  '''
def p_impresion(p):
  '''
  impresion : PRINTLN LPAREN valor RPAREN
  
  '''
#Axcel
def p_funcion(p):
  '''
  funcion : FN IDENTIFIER LPAREN parameters RPAREN LLLAVE programa RLLAVE
  
  '''

#Emilio
def p_parameters(p):
  '''
  parameters: IDENTIFIER COLON asig_data_type
              | IDENTIFIER COLON asig_data_type COMMA parameters
              | ''
  '''

#Emilio
def p_ingreso_datos(p):
  '''
  ingreso_datos : STD DOUBLE_COLON IO DOUBLE_COLON DOT STDIN LPAREN RPAREN DOT READLINE LPAREN REFERENCE MUT IDENTIFIER RPAREN

  '''

#Emilio
def p_asig_data_type(p):
  '''
  asig_data_type: data_type
                  | LPAREN some_data_type RPAREN
                  | LCORCH some_data_type PCORCH
  '''

#Emilio
def p_data_type(p):
  '''
  data_type : CHAR
              | signed_integer
              | unsigend_integer
              | float_type
              | BOOL
  '''
#Emilio
def p_signed_integer(p):
  '''
  signed_integer: I8
                | I16
                | I32
                | I64
                | I128
                | ISIZE
  '''
#Emilio
def p_unsigned_integer(p):
  '''
  unsigned_integer: U8
                  | U16
                  | U32
                  | U64
                  | U128
                  | USIZE
  '''
#Emilio
def p_float_type(p):
  '''
  float_type: F32
            | F64
  '''

#Emilio
def p_some_data_type(p):
  '''
  some_data_type: data_type
                | data_type COMMA some_data_type
  '''

#Emilio
def p_control_structure(p):
  '''
  control_structure: condicional
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
