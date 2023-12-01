import ply.yacc as sint
from tokens import tokens
from lexico import *
import tkinter as tk

#Fausto
def p_programa(p):
  '''programa : sentencias
            | sentencias programa

  '''
#Fausto & Emilio
#Emilio regla semántica 2: asignación de tipos de datos con sus valores correspondientes y declaración de variables sin valores
def p_asignacion_variable(p):
  '''asignacion_variable : LET IDENFTIFIER ASIG valor
                  | LET MUT ASIG valor
                  | LET IDENTIFIER COLON asignacion
                  | LET MUT IDENTIFIER COLON asignacion

  '''
#Emilio regla semántica 2
def p_declaracion_variable(p):
  '''declaracion_variable : LET IDENTIFIER
                          | LET MUT IDENTIFIER 
                          | LET IDENTIFIER COLON asig_data_type
                          | LET MUT IDENTIFIER COLON asig_data_type
  '''
#Emilio regla semántica 2
def p_asignacion(p):
  '''asignacion : string_asignacion
                | char_asignacion
                | numero_asignacion
                | boolean_asignacion
                | lista_asignacion
                | tupla_asignacion
  '''
#Emilio regla semántica 2
def p_string_asignacion(p):
  'string_asignacion : REFERENCE STR ASIG STRING'
def p_char_asignacion(p):
  'char_asignacion : CHAR ASIG CHARACTER'
def p_numero_asignacion(p):
  '''numero_asignacion  : signed_integer ASIG INTEGER
                        | signed_integer ASIG MINUS INTEGER
                        | unsigned_integer ASIG INTEGER
                        | float_type ASIG FLOAT
                        | float_type ASIG MINUS FLOAT
  '''
def p_boolean_asignacion(p):
  '''boolean_asignacion : BOOL ASIG TRUE
                        | BOOL ASIG FALSE
  '''
def p_lista_asignacion(p):
  'lista_asignacion : list_type ASIG arreglos'
def p_tupla_asignacion(p):
  'tupla_asignacion : tupla_type ASIG tuplas'
#Fausto
def p_comparacion(p):
  '''comparacion : valor EQ valor
                | valor NEQ valor
                | valor GEQ valor
                | valor LEQ valor
                | valor RIGHTARROW valor
                | valor LEFTARROW valor
  '''
#Fausto
def p_valor(p):
  '''
  valor : INTEGER 
          | FLOAT
          | IDENTIFIER
          | operacion
          | indexacion
          | arreglos
          | STRING
          | booleanos
  
  '''
#Axcel
def p_booleanos(p):
  '''
  booleanos : TRUE
            | FALSE
  '''

#Emilio
def p_vacio(p):
    'vacio :'
    pass

#Fausto
#Axcel Regla semantica #2: Semicolon al finalizar cada sentencia a excepcion de las que terminen en llaves
def p_sentencias(p):
  '''
  sentencias : asignacion_variable SEMICOLON
              | declaracion_variable SEMICOLON
              | impresion SEMICOLON
              | funcion 
              | ingreso_datos SEMICOLON
              | arreglos SEMICOLON
              | control_structure 
              | llamada SEMICOLON
  '''
#Axcel
def p_impresion(p):
  '''
  impresion : PRINTLN EXCLAMATION LPAREN valor RPAREN
            | PRINTLN EXCLAMATION LPAREN valor COMMA valores RPAREN
  
  
  '''
#Axcel
#Regla semantica #1: return statement opcional y solo uno
def p_funcion(p):
  '''
  funcion : FN IDENTIFIER LPAREN parameters RPAREN LLLAVE programa RLLAVE
          | FN MAIN LPAREN parameters RPAREN LLLAVE programa RLLAVE
          | FN MAIN LPAREN RPAREN LLLAVE programa RLLAVE
          | FN IDENTIFIER LPAREN RPAREN LLLAVE programa RLLAVE
          | FN IDENTIFIER LPAREN parameters RPAREN MINUS RIGHTARROW data_type LLLAVE programa retorno RLLAVE
          | FN IDENTIFIER LPAREN RPAREN MINUS RIGHTARROW data_type LLLAVE programa retorno RLLAVE
  
  '''
def p_retorno(p):
  '''
  retorno : RETURN valor SEMICOLON
  
  
  '''

#Emilio
def p_parameters(p):
  '''
  parameters : IDENTIFIER COLON asig_data_type
              | IDENTIFIER COLON asig_data_type COMMA parameters
              | vacio
  '''


#Emilio
def p_ingreso_datos(p):
  '''
  ingreso_datos : STD DOUBLE_COLON IO DOUBLE_COLON DOT STDIN LPAREN RPAREN DOT READLINE LPAREN REFERENCE MUT IDENTIFIER RPAREN

  '''

#Emilio
def p_asig_data_type(p):
  '''
  asig_data_type : data_type
                  | list_type
                  | tuple_type
  '''
def p_list_type(p):
  'list_type : LCORCH some_data_type RCORCH'
def p_tuple_type(p):
  'tuple_type : LPAREN some_data_type RPAREN'
#Emilio
def p_data_type(p):
  '''
  data_type : CHAR
              | REFERENCE STR
              | signed_integer
              | unsigned_integer
              | float_type
              | BOOL
  '''
#Emilio
def p_signed_integer(p):
  '''
  signed_integer : I8
                | I16
                | I32
                | I64
                | I128
                | ISIZE
  '''
#Emilio
def p_unsigned_integer(p):
  '''
  unsigned_integer : U8
                  | U16
                  | U32
                  | U64
                  | U128
                  | USIZE
  '''
#Emilio
def p_float_type(p):
  '''
  float_type : F32
            | F64
  '''

#Emilio
def p_some_data_type(p):
  '''
  some_data_type : data_type
                | data_type COMMA some_data_type
  '''

#Emilio
def p_control_structure(p):
  '''
  control_structure : condicional
  '''

#Axcel
def p_arreglos(p):
  '''
  arreglos : LCORCH valores RCORCH

  '''
#Emilio
def p_tuplas(p):
  'tuplas : LPAREN valores RPAREN'
#Axcel
def p_valores(p):
  '''
  valores : valor
          | valor COMMA valores

  '''
#Fausto
def p_error(p):
  print(f"Error sintáctico en la entrada {p}")
#Fausto
def p_conector(p):
  '''
  conector : AND 
            | OR
  '''
#Fausto
def p_proposicionC(p):
  '''proposicion : comparacion conector proposicion 
              | comparacion
  '''
#Fausto
def p_condicional(p):
  '''condicional : IF comparacion LLLAVE programa RLLAVE 
                | IF proposicion LLLAVE programa RLLAVE
  '''

#Fausto. Se asume que IDENTIFIER es numerico
def p_numeric_var(p):
  '''numeric : INTEGER
              | FLOAT
              | IDENTIFIER
  '''
#Fausto. Se asume IDENTIFIER STRING
def p_cadena(p):
  '''cadena : STRING
            | IDENTIFIER
  '''
#Axcel
#Fausto Regla Semántica 1: Permitir operaciones aritméticas entre valor numéricos.
#Fausto Regla semántica 2: Los strings solo pueden soportar el operador +, que representa concatenación
def p_operacion(p):
  '''operacion : numeric PLUS numeric
              | numeric MINUS numeric
              | numeric TIMES numeric
              | numeric DIVIDE numeric
              | numeric MOD numeric 
              | numeric INTD numeric
              | cadena PLUS cadena
  '''
#Axcel
def p_indexacion(p):
  '''indexacion : IDENTIFIER LCORCH INTEGER RCORCH

  '''

def p_llamada(p):
  '''llamada : IDENTIFIER LPAREN valores RPAREN
  
  '''

#Emilio regla semántica #1:  debe haber una función main en el programa
def p_main(p):
  '''main : FN MAIN LPAREN RPAREN LLLAVE programa RLLAVE
  '''

#Emilio
parser = sint.yacc()
'''while True:
   try:
       s = input('esp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)'''

def validarCodigo():
    error.pack_forget()
    result = parser.parse(entry.get(1.0, "end-1c"))
    error.pack()
    if(result==None):
      error.config(text="No hay ningun error en su codigo")
      error.pack()
    

window = tk.Tk()
window.title("Analizador Rust")
window.geometry("300x200")
text = tk.Label(window, text="Ingresa el codigo de Rust: ")
text.pack()
#codigoEntrada = tk.StringVar(value = "")
entry = tk.Text(window)
entry.pack()
button = tk.Button(window,
    text="Validar",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command= lambda: validarCodigo()
)
button.pack()
error = tk.Label(window, text="Error", fg="red")
#crear llamada al analizador sintactico
#crear label para respuesta de analizador sintactico
#crear errores personalizados a show error in label
window.mainloop()
