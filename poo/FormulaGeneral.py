
class FormulaGeneral:

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def potencia(self) -> float:
        return self.b * self.b

    def multiplicacion(self) -> float:
        return 4 * self.a * self.c

    def raiz(self) -> float:
        return math.sqrt(self.potencia() - self.multiplicacion())

    def division(self) -> []:
        x1 = (-self.b + self.raiz()) / (2 * self.a)
        x2 = (-self.b - self.raiz()) / (2 * self.a)
        return [x1, x2]

if _name_ == "_main_":
    resultado = FormulaGeneral(2, 4, 2)
    print(resultado.division())