import math

def addNumbers(a: float, b: float) -> int:
    """
    Función que retorna el piso entero de la suma de dos números flotantes.
    """
    return math.floor(a + b)


if __name__ == "__main__":
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    resultado = addNumbers(a, b)
    print(f"El piso entero de la suma de {a} y {b} es: {resultado}")

