from tkinter import Button, Entry, Label, Tk

root = Tk()


def hide_lbl(label):
    label.destroy()


def click_btn_1():
    txt_lbl = Label(root, text=f'{entry_1.get()} se guardo correctamente')
    txt_lbl.grid(row=0, column=1)
    root.after(3000, lambda: hide_lbl(txt_lbl))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")
    entry_5.delete(0, "end")
    entry_6.delete(0, "end")


# defino las etiquetas a usar

label_1 = Label(root, text="Producto:")
label_1.grid(row=0, column=0, sticky="w")
label_2 = Label(root, text="Descripcion:")
label_2.grid(row=1, column=0, sticky="w")
label_3 = Label(root, text="Costo:")
label_3.grid(row=2, column=0, sticky="w")
label_4 = Label(root, text="Precio Venta:")
label_4.grid(row=3, column=0, sticky="w")
label_5 = Label(root, text="Proveedor:")
label_5.grid(row=4, column=0, sticky="w")
label_6 = Label(root, text="Stock:")
label_6.grid(row=5, column=0, sticky="w")

# Defino los campos donde se ingresara el texto
entry_1 = Entry(root)
entry_1.grid(row=0, column=1)
entry_2 = Entry(root)
entry_2.grid(row=1, column=1)
entry_3 = Entry(root)
entry_3.grid(row=2, column=1)
entry_4 = Entry(root)
entry_4.grid(row=3, column=1)
entry_5 = Entry(root)
entry_5.grid(row=4, column=1)
entry_6 = Entry(root)
entry_6.grid(row=5, column=1)

btn_1 = Button(root, text="Agregar", command=click_btn_1)
btn_1.grid(row=6, column=0)

root.mainloop()
