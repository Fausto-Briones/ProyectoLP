#Programa que recibe codigo en Rust
import ply.lex as lex
import functions,tokens, reserved_words,symbols_regex

if __name__ == "__main__":
  lexer = lex.lex()
  numero=0
  while (numero < 1 or numero > 3):
    numero = input("Ingrese número del 1 al 3")

  archivo = open ("Algoritmos/Algoritmo"+numero+".txt")
  while(r"[^END]"):
    lexer.input(archivo.read())
  # Enviando el código
  lexer.input(code)

  # Tokenizar
  for token in lexer:
    print(token)
  
