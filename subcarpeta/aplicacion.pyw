""" 
    Contiene el loggin de la aplicación principal; en ella se le solicitará al
    usuario que teclee su usuario y contraseña. 
    Contiene las etiquetas, dos entry y dos botones uno para entrar y el otro para salir. 
""" 

from tkinter import * 
from tkinter import messagebox

# ---------------------------- Logueo principal: ---------------------------------------
# ---------------------------- Ventana principal: --------------------------------------
logueo = Tk() 
logueo.title("Logueo de la aplicación")
logueo.geometry("500x400")
logueo.resizable(0, 0) 

# ---------------------------- Variables de entrada: -----------------------------------
elUsuario = StringVar() 
laClave = StringVar() 

# ---------------------------- Marcos del logueo: --------------------------------------
panelEntrada = Frame(logueo, width = 500, height = 300)
panelControl = Frame(logueo, width = 500, height = 100) 

panelEntrada.pack() 
panelControl.pack() 

panelEntrada.config(bg = "lightblue")
panelControl.config(bg = "white") 

# ----------------------------- Widgets de la aplicación: -------------------------------



logueo.mainloop()