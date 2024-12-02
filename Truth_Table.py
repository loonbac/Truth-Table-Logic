def validar_binario(*valores):
    for valor in valores:
        if valor not in (0, 1):
            raise ValueError("Todos los valores deben ser 0 o 1.")

def logica_not(valor):
    validar_binario(valor)
    return 1 - valor

def logica_and(var1, var2):
    validar_binario(var1, var2)
    return var1 & var2

def logica_or(var1, var2):
    validar_binario(var1, var2)
    return var1 | var2
