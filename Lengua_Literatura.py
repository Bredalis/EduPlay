
from Estructura_Ventanas import *

# Lengua y Literatura (Area)

trabajos = ['Escritor/a', 'Editor/a', 
	'Periodista', 'Traductor/a', 
	'Profesor/a de lengua y literatura'
]

definicion = '''

¡Aquí es donde los libros se vuelven aventuras! Leemos historias 
emocionantes, escribimos cuentos fantásticos y descubrimos el poder 
de las palabras. Aprendemos a comunicarnos mejor y a expresar nuestros 
pensamientos y sentimientos.
'''

lengua_literatura = EstructuraDeVentanas(trabajos)
lengua_literatura.crear_ventana()
lengua_literatura.obtener_titulo('Lengua y Literatura')
lengua_literatura.crear_subventana()
lengua_literatura.obtener_definicion(definicion)
lengua_literatura.mostrar_subtitulo()
lengua_literatura.mostrar_trabajos()
lengua_literatura.cerrar_ventana()