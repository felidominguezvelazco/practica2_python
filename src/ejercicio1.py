def obtener_lineas(texto):
    return texto.strip().split("\n")


def contar_lineas(texto):
    return len(obtener_lineas(texto))


def contar_palabras(texto):
    return len(texto.split())


def promedio_palabras_por_linea(texto):
    lineas = obtener_lineas(texto)
    total_palabras = sum(len(linea.split()) for linea in lineas)
    return total_palabras / len(lineas)


def lineas_mayor_promedio(texto):
    lineas = obtener_lineas(texto)
    promedio = promedio_palabras_por_linea(texto)

    resultado = []
    for linea in lineas:
        cantidad = len(linea.split())
        if cantidad > promedio:
            resultado.append((linea, cantidad))

    return resultado