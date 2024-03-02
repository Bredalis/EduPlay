
from Estructura_Ventanas import *

# Artes Visuales y Música (Area)

trabajos = ['Fotógrafo/a', 'Músico/a', 
	'Compositor/a', 'Director/a', 
	'Animador'
]

definicion = '''

¡Aquí es donde la creatividad se vuelve real! Dibujamos, 
pintamos, y creamos obras de arte increíbles. También exploramos 
diferentes sonidos, ritmos y melodías en la música. ¡Es como un concierto 
y una galería de arte en la escuela!
'''

artes_visuales = EstructuraDeVentanas(trabajos)
artes_visuales.crear_ventana()
artes_visuales.obtener_titulo('Artes Visuales y Música')
artes_visuales.crear_subventana()
artes_visuales.obtener_definicion(definicion)
artes_visuales.mostrar_subtitulo()
artes_visuales.mostrar_trabajos()
artes_visuales.cerrar_ventana()