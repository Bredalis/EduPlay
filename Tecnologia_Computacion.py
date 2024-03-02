
from Estructura_Ventanas import *

# Tecnologia y Computacion (Area)

trabajos = ['Ingeniero/a de software', 'Desarrollador/a web', 
	'Analista de sistemas', 'Administrador/a de bases de datos', 
	'Especialista en ciberseguridad'
]

definicion = '''

La tecnología y la computación son como magia para las máquinas. 
Son las herramientas y los trucos que usamos en las computadoras 
y teléfonos para hacer cosas increíbles, como jugar juegos, hablar 
con amigos en línea, aprender en la escuela y mucho más.
'''

tecnologia_computacion = EstructuraDeVentanas(trabajos)
tecnologia_computacion.crear_ventana()
tecnologia_computacion.obtener_titulo('Tecnología y Computación')
tecnologia_computacion.crear_subventana()
tecnologia_computacion.obtener_definicion(definicion)
tecnologia_computacion.mostrar_subtitulo()
tecnologia_computacion.mostrar_trabajos()
tecnologia_computacion.cerrar_ventana()