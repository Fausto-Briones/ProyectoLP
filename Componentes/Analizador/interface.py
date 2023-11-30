import tkinter as tk
from main import *

def validarCodigo():
    result = parser.parse(entry.get(1.0, "end-1c"))
    print(result)

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
#crear llamada al analizador sintactico
#crear label para respuesta de analizador sintactico
#crear errores personalizados a show error in label
window.mainloop()
