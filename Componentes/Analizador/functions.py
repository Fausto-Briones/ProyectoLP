import ply.lex as lex
from reserved_words import reserved
def t_IDENTIFIER(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'IDENTIFIER')
  return t
  
# Expresión regular para números flotantes, incluye cast
def t_FLOAT(t):
  r'(\d+\.\d+)|(\d+\.)'
  t.value = float(t.value)
  return t

# Expresion regular para enteros
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Expresión regular para reconocer strings
def t_STRING(t):
  r'\".*?\"'
  t.value = t.value[1:-1]
  return t

#Salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Token de error
def t_error(t):
  print(f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}")
  t.lexer.skip(1)

t_ignore = ' \t'