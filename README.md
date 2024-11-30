# Proyecto de Lógica Booleana en Python
![Logo](https://i.imgur.com/4Yi4QWM.png)
## Lógica Booleana

La lógica booleana es una forma de algebra que se utiliza en computación y matemáticas. Se basa en valores binarios, que son 0 y 1. En este proyecto, implemento tres funciones que representan las operaciones lógicas más comunes:

## 1. NOT:
Esta operación invierte el valor. Si el valor es 1, devuelve 0, y si es 0, devuelve 1.

```python
    # Validar que el valor proporcionado sea binario (0 o 1)
    validar_binario(valor)
    # Restar el valor a 1 para calcular su NOT lógico
    # Si valor es 1, devolver 0
    # Si valor es 0, devolver 1
    return 1 - valor

```

## 2. AND:
 Esta operación devuelve 1 solo si ambos valores son 1. Si alguno de los valores es 0.

```python
    # Validar que ambos valores proporcionados sean binarios (0 o 1)
    validar_binario(var1, var2)
    # Usar la operación AND bit a bit (&) para calcular el resultado
    # Si ambos valores son 1, devolver 1
    # En cualquier otro caso, devolver 0
    return var1 & var2
```

## 3. OR:
 Esta operación devuelve 1 si al menos uno de los valores es 1. Solo devuelve 0 si ambos valores son 0.

```python
    # Validar que ambos valores proporcionados sean binarios (0 o 1)
    validar_binario(var1, var2)
    # Usar la operación OR bit a bit (|) para calcular el resultado
    # Si al menos uno de los valores es 1, devolver 1
    # Si ambos valores son 0, devolver 0
    return var1 | var2
```
## 4. Funcion de Validacion
La función validar_binario centraliza la validación, lo que reduce la repetición.

```python
    # Iterar sobre todos los valores proporcionados
    for valor in valores:
        # Si el valor no es 0 o 1
        if valor not in (0, 1):
            # Lanzar un error indicando que los valores deben ser binarios
            raise ValueError("Todos los valores deben ser 0 o 1.")
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
