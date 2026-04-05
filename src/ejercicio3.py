def filtrar_spoilers(texto, palabras_spoiler):
    palabras = texto.split()

    resultado = []

    spoilers_lower = [p.lower() for p in palabras_spoiler]

    for palabra in palabras:
        palabra_limpia = palabra.strip(".,").lower()

        if palabra_limpia in spoilers_lower:
            nueva = "*" * len(palabra_limpia)
            
            # mantener puntuación si tenía
            if palabra.endswith(","):
                nueva += ","
            elif palabra.endswith("."):
                nueva += "."

            resultado.append(nueva)
        else:
            resultado.append(palabra)

    return " ".join(resultado)                   