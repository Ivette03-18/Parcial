import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Conexión a la base de datos
conn = sqlite3.connect('asistencia.db')
c = conn.cursor()

# Creación de la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS asistencia (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             estudiante TEXT NOT NULL,
             fecha TEXT NOT NULL,
             estado TEXT NOT NULL,
             razon TEXT)''')

conn.commit()

# Función para registrar la asistencia
def registrar_asistencia():
    estudiante = entry_estudiante.get()
    estado = var_estado.get()
    razon = entry_razon.get()
    fecha = datetime.now().strftime('%Y-%m-%d')

    if estudiante and estado:
        c.execute("INSERT INTO asistencia (estudiante, fecha, estado, razon) VALUES (?, ?, ?, ?)",
                  (estudiante, fecha, estado, razon if estado == 'Permiso' else None))
        conn.commit()
        messagebox.showinfo("Éxito", "Asistencia registrada correctamente")
        entry_estudiante.delete(0, tk.END)
        entry_razon.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Por favor, complete todos los campos necesarios.")

# Interfaz gráfica
root = tk.Tk()
root.title("Registro de Asistencia")

# Etiquetas y entradas
tk.Label(root, text="Nombre del Estudiante:").grid(row=0, column=0, padx=10, pady=10)
entry_estudiante = tk.Entry(root)
entry_estudiante.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Estado:").grid(row=1, column=0, padx=10, pady=10)
var_estado = tk.StringVar(value="Presente")
tk.Radiobutton(root, text="Presente", variable=var_estado, value="Presente").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Permiso", variable=var_estado, value="Permiso").grid(row=1, column=2, sticky="w")
tk.Radiobutton(root, text="Ausente", variable=var_estado, value="Ausente").grid(row=1, column=3, sticky="w")

tk.Label(root, text="Razón (si aplica):").grid(row=2, column=0, padx=10, pady=10)
entry_razon = tk.Entry(root)
entry_razon.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="we")

# Botón para registrar
btn_registrar = tk.Button(root, text="Registrar Asistencia", command=registrar_asistencia)
btn_registrar.grid(row=3, column=0, columnspan=4, padx=10, pady=20)

root.mainloop()

# Cierre de la conexión
conn.close()
