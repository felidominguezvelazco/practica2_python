def convertir_a_segundos(duracion):
    minutos, segundos = duracion.split(":")
    return int(minutos) * 60 + int(segundos)


def convertir_a_minutos(segundos):
    m = segundos // 60
    s = segundos % 60
    return m, s


def duracion_total(playlist):
    total = 0
    for cancion in playlist:
        total += convertir_a_segundos(cancion["duration"])
    return total


def cancion_mas_larga(playlist):
    return max(playlist, key=lambda c: convertir_a_segundos(c["duration"]))


def cancion_mas_corta(playlist):
    return min(playlist, key=lambda c: convertir_a_segundos(c["duration"]))