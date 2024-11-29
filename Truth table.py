def logica_not(valor):
    if valor == 1:
        return 0
    elif valor == 0:
        return 1
    else:
        raise ValueError("El valor debe ser 0 o 1")
    
def logica_and(var1, var2):
    if (var1 == 0 or var1 == 1) and (var2 == 0 or var2 == 1):
        if var1 == 1 and var2 == 1:
            return 1
        else:
            return 0
    else:
        raise ValueError("Ambas variables deben ser 0 o 1")
    
def logica_or(var1, var2):
    if (var1 == 0 or var1 == 1) and (var2 == 0 or var2 == 1):
        if var1 == 0 and var2 == 0:
            return 0
        else:
            return 1
    else:
        raise ValueError("Ambas variables deben ser 0 o 1")