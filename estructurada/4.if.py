if _name_ == "_main_":
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    c = int(input("Ingrese uno más: "))

if a > b:
    if a > c:
        print(f"El mayor es {a}")
    else:
        print(f"El mayor es {c}")
elif b > c:
    print(f"El mayor es {b}")
else:
    print(f"El mayor es {c}")
