
from Estructura_Ventanas import *

# Matematicas (Area)

trabajos = ['Ingeniero/a', 'Actuario/a', 
	'Analista de datos', 'Científico/a de datos', 
	'Programador/a'
]

definicion = '''

¡Aquí es donde los números se vuelven divertidos! Resolvemos acertijos, 
jugamos con formas y descubrimos patrones en todo. Las matemáticas nos 
ayudan a resolver problemas y a entender el mundo de una manera genial y lógica.
'''

matematicas = EstructuraDeVentanas(trabajos)
matematicas.crear_ventana()
matematicas.obtener_titulo('Matemáticas')
matematicas.crear_subventana()
matematicas.obtener_definicion(definicion)
matematicas.mostrar_subtitulo()
matematicas.mostrar_trabajos()
matematicas.cerrar_ventana()