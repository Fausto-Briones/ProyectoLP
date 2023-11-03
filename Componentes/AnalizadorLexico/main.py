#Programa que recibe codigo en Rust
import ply.lex as lex
import functions,tokens, reserved_words,symbols_regex

if __name__ == "__main__":
  lexer = lex.lex()
  entrada = input(code)
  while(r"[^END]"):
    lexer.input(entrada)
  # Enviando el código
  lexer.input(code)

  # Tokenizar
  for token in lexer:
    print(token)
  
