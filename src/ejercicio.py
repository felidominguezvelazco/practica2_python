def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            inicio = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - inicio + desplazamiento) % 26 + inicio)
        else:
            resultado += char
    return resultado