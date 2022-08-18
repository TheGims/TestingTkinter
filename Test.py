import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg = "blue")
#etiqueta.pack(side = tkinter.BOTTOM)
etiqueta.pack(fill = tkinter.X)
ventana.mainloop()
