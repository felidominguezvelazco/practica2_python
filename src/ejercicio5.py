def calcular_costo_envio(peso, zona):
    tarifas = {
        "local": [500, 1000, 2000],
        "regional": [1000, 2500, 4500],
        "nacional": [2000, 5000, 8000]
    }
    
    if zona not in tarifas:
        return None  # Indicamos zona no válida
    
    if peso <= 1:
        idx = 0
    elif peso <= 5:
        idx = 1
    else:
        idx = 2
    
    return tarifas[zona][idx]