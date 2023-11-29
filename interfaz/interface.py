import tkinter as tk
window = tk.Tk()
window.title("Analizador Rust")
window.geometry("300x200")
text = tk.Label(window, text="Ingresa el codigo de Rust: ")
text.pack()
entry = tk.Text(window)
entry.pack()
window.mainloop()
