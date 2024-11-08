if _name_ == "_main_":
    def suma(x, y):
        return x + y

    Suma = lambda x, y: x + y
    resultado_suma = Suma(3, 4)
    print("Resultado de la suma:", resultado_suma)

    Resta = lambda x, y: x - y
    resultado_resta = Resta(3, 4)
    print("Resultado de la resta:", resultado_resta)

    Potencia = lambda x: x ** 2
    resultado_potencia = Potencia(9)
    print("Resultado de la potencia:", resultado_potencia)