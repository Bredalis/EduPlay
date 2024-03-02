
from Estructura_Ventanas import *

# Ciencias Sociales (Area)

trabajos = ['Historiador/a', 'Antropólogo/a', 
	'Sociólogo/a', 'Geógrafo/a', 
	'Diplomático/a'
]

definicion = '''

¡Viajamos en el tiempo y alrededor del mundo! 
Aprendemos sobre civilizaciones antiguas, exploradores 
valientes, y culturas fascinantes. Descubrimos por qué 
los mapas son tan importantes y cómo las personas viven 
en diferentes partes del planeta.
'''

ciencias_sociales = EstructuraDeVentanas(trabajos)
ciencias_sociales.crear_ventana()
ciencias_sociales.obtener_titulo('Ciencias Sociales')
ciencias_sociales.crear_subventana()
ciencias_sociales.obtener_definicion(definicion)
ciencias_sociales.mostrar_subtitulo()
ciencias_sociales.mostrar_trabajos()
ciencias_sociales.cerrar_ventana()