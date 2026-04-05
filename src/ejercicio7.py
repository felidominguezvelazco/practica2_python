import random

def sorteo_amigo_invisible(nombres):
    # limpiar espacios
    nombres = [n.strip() for n in nombres]

    # validar mínimo 3
    if len(nombres) < 3:
        return None, "Debe haber al menos 3 participantes"

    # validar duplicados (ignorando mayúsculas)
    normalizados = [n.lower() for n in nombres]
    if len(normalizados) != len(set(normalizados)):
        return None, "No debe haber nombres duplicados"

    # mezclar copia
    mezclados = nombres[:]
    random.shuffle(mezclados)

    # asegurar que nadie se tenga a sí mismo
    for i in range(len(nombres)):
        if nombres[i] == mezclados[i]:
            # solución simple: rotar la lista
            mezclados = mezclados[1:] + mezclados[:1]
            break

    # generar asignaciones
    asignaciones = {}
    for i in range(len(nombres)):
        asignaciones[nombres[i]] = mezclados[i]

    return asignaciones, None