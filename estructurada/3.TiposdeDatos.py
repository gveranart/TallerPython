if _name_ == '_main_':
    # Tipos de datos básicos
    entero = 42                         # int
    decimal = 3.14                      # float
    complejo = 2 + 3j                   # complex
    booleano = True
    cadena = "Hola, Python!"
    binario = bytes([50, 100, 150])     # bytes

    print("Tipos básicos:")
    print("Entero:", entero)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Booleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario, "\n")

    # Estructuras de datos avanzadas
    lista = [1, 2, 3, "cuatro"]          # list
    tupla = (5, 6, 7, "ocho")            # tuple
    conjunto = {9, 10, "once", "doce"}   # set
    diccionario = {"clave1": "valor1", "clave2": 20}

    print("Estructuras avanzadas:")
    print("Lista:", lista)
    print("Tupla:", tupla)
    print("Conjunto:", conjunto)
    print("Diccionario:", diccionario, "\n")

    nulo = None
    rango = range(3)
    print("Tipos especiales:")
    print("Nulo:", nulo)
    print("Rango:", list(rango))  # Convertimos a lista para mostrar los elementos

    # Ejemplo de iteración con el tipo range
    print("\nIterando sobre el rango:")
    for numero in rango:
        print(numero)
        print(numero)
        print(numero)