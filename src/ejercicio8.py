def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    for char in texto:
        if char.islower():
            base = ord('a')
            nuevo = (ord(char) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo)

        elif char.isupper():
            base = ord('A')
            nuevo = (ord(char) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo)

        else:
            resultado += char  # no modificar

    return resultado


def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)