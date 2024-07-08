import tkinter as tk
from tkinter import filedialog

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Adres - Interfaz de scraping")
        self.label = tk.Label(master, text="Seleccione un archivo Excel:")
        self.label.pack()
        self.button = tk.Button(master, text="Subir archivo", command=self.upload_file)
        self.button.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            print(f"Archivo seleccionado: {file_path}")
            # Llamada a la función de scraping aquí

root = tk.Tk()
gui = GUI(root)
root.mainloop()