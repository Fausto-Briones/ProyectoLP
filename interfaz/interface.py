import tkinter as tk
window = tk.Tk()
window.title("Analizador Rust")
window.geometry("300x200")
text = tk.Label(window, text="Ingresa el codigo de Rust: ")
text.pack()
entry = tk.Text(window)
entry.pack()
button = tk.Button(window,
    text="Validar",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
#crear llamada al analizador sintactico
#crear label para respuesta de analizador sintactico
#crear errores personalizados a show error in label
window.mainloop()
