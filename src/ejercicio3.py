import re

def filtrar_spoilers(texto, palabras):
    """
    Reemplaza en 'texto' todas las palabras de la lista 'palabras'
    por asteriscos de la misma longitud, sin distinguir mayúsculas/minúsculas.
    """
    for palabra in palabras:
        palabra = palabra.strip()
        texto = re.sub(re.escape(palabra), '*' * len(palabra), texto, flags=re.IGNORECASE)
    return texto                       