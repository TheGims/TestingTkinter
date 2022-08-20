import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
def saludo(nombre):
        print("Hola " + nombre)
boton1 = tkinter.Button(ventana, text = "Presiona", command = lambda: saludo("python"))
boton1.pack()
ventana.mainloop()
