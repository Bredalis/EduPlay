
import tkinter as tk

class EstructuraDeVentanas:
	def __init__(self, trabajos):
		self.trabajos = trabajos

	def crear_ventana(self):

		self.ventana = tk.Tk()
		self.ventana.title('EduPlay')
		self.ventana.geometry('350x500')
		self.ventana.resizable(0, 0)
		self.ventana.config(bg = '#5390d9')
		self.ventana.iconbitmap('Logo_BlancoNegro.ico')

	def obtener_titulo(self, titulo):
		tk.Label(self.ventana, text = titulo, 
			bg = '#5390d9', font = ('Helvetica', 18),
			fg = 'white', pady = 20).pack()

	def crear_subventana(self):

		# Ventana de contenido

		self.subventana = tk.Frame(self.ventana, width = 300, 
			height = 400, bg = '#64dfdf')
		self.subventana.pack(pady = 10)

	def obtener_definicion(self, contenido):

		# Definicion del titulo
		self.contenido = contenido

	def mostrar_subtitulo(self):
		tk.Label(self.subventana, text = self.contenido, wraplength = 250, 
			bg = '#64dfdf').place(x = 25, y = 20)
		tk.Label(self.subventana, text = 'Futuros Trabajos', font = ('Helvetica', 18),
			fg = 'white', bg = '#64dfdf').place(x = 50, y = 190)

	def mostrar_trabajos(self):
		tk.Label(self.subventana, text = f'- {self.trabajos[0]}', bg = '#64dfdf').place(x = 50, y = 235)
		tk.Label(self.subventana, text = f'- {self.trabajos[1]}', bg = '#64dfdf').place(x = 50, y = 255)
		tk.Label(self.subventana, text = f'- {self.trabajos[2]}', bg = '#64dfdf').place(x = 50, y = 275)
		tk.Label(self.subventana, text = f'- {self.trabajos[3]}', bg = '#64dfdf').place(x = 50, y = 295)
		tk.Label(self.subventana, text = f'- {self.trabajos[4]}', bg = '#64dfdf').place(x = 50, y = 315)

	def cerrar_ventana(self):
		self.ventana.mainloop()