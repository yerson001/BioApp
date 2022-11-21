 Saber la cantidad de caracteres que tiene cada cadena
Identificar que tipo de cadena es ARN, ADN o proteina


Alineamientos que debe tener:
        Global
        Local
        Ordenamiento estrella

Visual:
Alineamientos con colores A- AA -A 
Cantidad de alineamientos (5)
score

Matrices de Pesos:
Blosum


Estructura secundaria: las 2 tecnincas (cambios de signos)

Entrega del trabajo final es el dia del examen final

Import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("<path/image_name>")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=<x_coordinate>, y=<y_coordinate>)
root.mainloop()
