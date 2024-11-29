# Proyecto de Lógica Booleana en Python
![Logo](https://i.imgur.com/4Yi4QWM.png)
## Lógica Booleana

La lógica booleana es una forma de algebra que se utiliza en computación y matemáticas. Se basa en valores binarios, que son 0 y 1. En este proyecto, implemento tres funciones que representan las operaciones lógicas más comunes:

## 1. NOT:
Esta operación invierte el valor. Si el valor es 1, devuelve 0, y si es 0, devuelve 1.

```python
# Si el Valor es 1
    if valor == 1:
        # Devolver 0
        return 0
# Si el Valor es 0
    elif valor == 0:
        # Devolver 1
        return 1
```

## 2. AND:
 Esta operación devuelve 1 solo si ambos valores son 1. Si alguno de los valores es 0.

```python
# Si el Valor del Bit 1 es igual a 0 o 1 y si el Valor del Bit 2 es igual a 0 o 1 entonces
    if (var1 == 0 or var1 == 1) and (var2 == 0 or var2 == 1):
        # Si el Valor del Bit 1 es igual a 1 y el Valor del Bit 2 es igual a 1 
        if var1 == 1 and var2 == 1:
            # Devolver 1
            return 1
        # Sino
        else:
            # Devolver 0
            return 0
```

## 3. OR:
 Esta operación devuelve 1 si al menos uno de los valores es 1. Solo devuelve 0 si ambos valores son 0.

```python
# Si el Valor del Bit 1 es igual a 0 o 1 y si el Valor del Bit 2 es igual a 0 o 1 entonces
    if (var1 == 0 or var1 == 1) and (var2 == 0 or var2 == 1):
        # Si el Valor del Bit 1 es igual a 0 y el Valor del Bit 2 es igual a 0 
        if var1 == 0 and var2 == 0:
            # Devolver 0
            return 0
        # Sino
        else:
            # Devolver 1
            return 1
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
