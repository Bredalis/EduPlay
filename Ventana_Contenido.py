
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title('EduPlay')
ventana.geometry('350x500')
ventana.resizable(0, 0)
ventana.config(bg = '#5390d9')

ventana.iconbitmap('Logo_BlancoNegro.ico')

# Mostrar otras ventanas

def mostrar_ventana(url):
	modulo = open(url, encoding = 'utf-8').read()
	exec(modulo)	

# Mostrar manual

contenido = open('C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Python/Programas/Manual.txt').read()
exec(contenido)

tk.Label(ventana, text = 'EduPlay', bg = '#5390d9', font = ('Helvetica', 18),
	fg = 'white', pady = 20).pack()

tk.Label(ventana, text = 'Has click en alguna area para saber más', 
	bg = '#5390d9', font = ('Helvetica'), fg = 'white').pack()

# Ventana de contenido

subventana = tk.Frame(ventana, width = 300, height = 500, bg = '#64dfdf')
subventana.pack(pady = 30)

tk.Button(subventana, text = 'Matemáticas', command = lambda: mostrar_ventana('Matematica.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 30, padx = 100)
tk.Button(subventana, text = 'Lengua y Literatura', command = lambda: mostrar_ventana('Lengua_Literatura.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 10)
tk.Button(subventana, text = 'Tecnología y Computación', command = lambda: mostrar_ventana('Tecnologia_Computacion.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 10)
tk.Button(subventana, text = 'Ciencias Sociales', command = lambda: mostrar_ventana('Ciencias_Sociales.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 10)
tk.Button(subventana, text = 'Artes Visuales y Música', command = lambda: mostrar_ventana('Artes_Visuales.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 10)
tk.Button(subventana, text = 'Educación Cívica y Ética', command = lambda: mostrar_ventana('Educacion_Civica.py'), 
	bg = '#33415c', fg = 'white', activebackground = '#ccdbfd').pack(pady = 30)

manual('Manual_EduPlay.txt', 'Logo_BlancoNegro.ico', '#64dfdf')

ventana.mainloop()