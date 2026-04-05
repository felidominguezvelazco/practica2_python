def validar_email(email):
    """
    Valida un email según los criterios:
    - Contiene exactamente un '@'.
    - Tiene al menos un carácter antes del '@'.
    - Tiene al menos un punto (.) después del '@'.
    - No empieza ni termina con '@' ni con '.'.
    - La parte después del último punto tiene al menos 2 caracteres.
    """
    
    if email.count("@") != 1:
        return False
    elif email.startswith("@") or email.endswith("@"):
        return False
    else:
        usuario, dominio = email.split("@")
        if len(usuario) < 1:
            return False
        elif "." not in dominio:
            return False
        elif email.startswith(".") or email.endswith("."):
            return False
        elif len(dominio.split(".")[-1]) < 2:
            return False
        else:
            return True