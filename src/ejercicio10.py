def puntaje_ronda(scores_ronda):
    """
    Recibe el diccionario de puntajes de la ronda y devuelve
    un diccionario con la suma de los puntajes de cada cocinero.
    """
    total_ronda = {}
    for cocinero, jueces in scores_ronda.items():
        total_ronda[cocinero] = sum(jueces.values())
    return total_ronda

def actualizar_acumulados(acumulados, ronda_totales):
    """
    Actualiza los puntajes acumulados, rondas ganadas, mejor ronda y cantidad de rondas.
    """
    max_puntaje = max(ronda_totales.values())
    for cocinero, pts in ronda_totales.items():
        acumulados[cocinero]['puntaje'] += pts
        acumulados[cocinero]['rondas'] += 1
        if pts > acumulados[cocinero]['mejor_ronda']:
            acumulados[cocinero]['mejor_ronda'] = pts
        if pts == max_puntaje:
            acumulados[cocinero]['rondas_ganadas'] += 1
    return acumulados

def promedio_ronda(acumulado):
    """
    Calcula promedio por ronda de cada cocinero
    """
    return acumulado['puntaje'] / acumulado['rondas'] if acumulado['rondas'] > 0 else 0

def ordenar_tabla(acumulados):
    """
    Devuelve una lista de tuplas ordenada por puntaje total descendente
    """
    tabla = []
    for cocinero, datos in acumulados.items():
        tabla.append((cocinero, datos['puntaje'], datos['rondas_ganadas'], datos['mejor_ronda'], promedio_ronda(datos)))
    tabla.sort(key=lambda x: x[1], reverse=True)
    return tabla