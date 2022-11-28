from tkinter import *  # libreria

raiz=Tk()


raiz.title("Ventana de Prueba")

# cambio de icono ( coversor.icon)
#raiz.iconbitmap("gato.ico")

raiz.resizable(0,0) # inabilita redimensionar la ventana
# cambiar tamaño de Ventana
raiz.geometry("650x350")
# cambio de color
raiz.config(bg="green")

raiz.title("Aplicacion grafica en pyhon")

etiqueta =Label(raiz,text="Hola Mundo con Python")

boton=Button(raiz,text="OK")

etiqueta.pack()

boton.pack()

raiz.mainloop()

