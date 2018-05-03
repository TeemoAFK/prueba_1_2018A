import math
valor = 0


def cubo(lado):
    return lado * lado * lado


def piracuadrada(area,base):
    return (base*area)/3

def fun2():
    return 0


def esfera(radio):
    return 3 / 4 * math.pi * radio


opcion = 0
while (opcion != 5):
    print("PRUEBA 1")
    print("Volumen de figuras geometricas")
    print("1. Cubo")
    print("2. Piramide Cuadrada")
    print("3. ")
    print("4. Esfera")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        valor = float(input("Ingrese el lado del cubo"))
        print("Resultado", cubo(valor))
    if (opcion == 2):
        valor=float(input("Ingrese el area de la base"))
        valor1=float(input("Ingrese la altura"))
        piracuadrada(valor,valor1)
    if (opcion == 3):
        func2()
    if opcion == 4:
        valor = float(input("Ingrese el radio de la esfera"))
        esfera(valor)
    if opcion == 5:
        print("Salir")
    if opcion >= 6:
        print("Seleccione una opcion correcta")
