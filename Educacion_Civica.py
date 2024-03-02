
from Estructura_Ventanas import *

# Educacion Civica y Etica (Area)

trabajos = ['Abogado/a', 'Político/a', 
	'Defensor/a de derechos humanos', 'Activista social', 
	'Ético/a en empresas'
]

definicion = '''

¡Aprendemos cómo ser súper héroes en la vida real! 
Descubrimos sobre la importancia de ser buenos ciudadanos, 
respetar a los demás y hacer lo correcto. Hablamos sobre valores 
como la amistad, la honestidad y la justicia.
'''

educacion_civica = EstructuraDeVentanas(trabajos)
educacion_civica.crear_ventana()
educacion_civica.obtener_titulo('Educación Cívica y Ética')
educacion_civica.crear_subventana()
educacion_civica.obtener_definicion(definicion)
educacion_civica.mostrar_subtitulo()
educacion_civica.mostrar_trabajos()
educacion_civica.cerrar_ventana()