#Programa que recibe codigo en Rust
import ply.lex as lex
from reserved_words import reserved
from tokens import *
from functions import *
from symbols_regex import *

lexer = lex.lex()
'''if __name__ == "__main__":
  
  numero= 0
  while (numero < 1 or numero > 3):
    numero = int(input("Ingrese número del 1 al 3\n"))

  archivo = open ("Algoritmos/Algoritmo"+str(numero)+".txt")
  #while(r"[^END]"):
  lexer.input(archivo.read())
  # Enviando el código
  #lexer.input(code)

  # Tokenizar
  for token in lexer:
    print(token)
  
'''