
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title('EduPlay')
ventana.geometry('350x500')
ventana.resizable(0, 0)
ventana.config(bg = '#5390d9')

ventana.iconbitmap('Logo_BlancoNegro.ico')

def ventana_contenido(url = 'Ventana_Contenido.py'):
	modulo = open(url, encoding = 'utf-8').read()
	exec(modulo)

tk.Label(ventana, text = 'EduPlay', bg = '#5390d9', font = ('Helvetica', 24),
	fg = 'white', pady = 65).pack()

# Logo

img = Image.open('Logo_NegroBlanco.ico')
logo = ImageTk.PhotoImage(img)

contenido = tk.Label(ventana, image = logo, bg = '#5390d9')
contenido.pack()

tk.Button(ventana, text = '¡Iniciar!', width = 10, bg = '#33415c', fg = 'white', 
	activebackground = '#ccdbfd', command = ventana_contenido).pack(pady = 30)

ventana.mainloop()