import math
valor=0
valor1=0

def cubo(lado):
    return lado * lado * lado

def piracuadrada(base, altura):
    areabase = base**2
    return (areabase * altura) / 3

def piratriangular(base, altura):
    areabase=(base*altura)/2
    return (areabase*altura)/3

def esfera(radio):
    return 3 / 4 * math.pi * radio

opcion = 0
while (opcion != 5):
    print("PRUEBA 1")
    print("\tVolumen de figuras Geometricas")
    print("Por favor seleccione una figura para obtener el volumen:")
    print("1. Cubo")
    print("2. Piramide base Cuadrada")
    print("3. Piramide base Triangular")
    print("4. Esfera")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        valor = float(input("Ingrese el lado del cubo: "))
        print("Resultado: ", cubo(valor))
    if (opcion == 2):
        valor=float(input("Ingrese la base: "))
        valor1=float(input("Ingrese la altura: "))
        print("Resultado: ", piracuadrada(valor,valor1))
    if (opcion == 3):
        valor = float(input("Ingrese la altura: "))
        valor1 = float(input("Ingrese la base: "))
        print("Resultado: ", piratriangular(valor, valor1))
    if opcion == 4:
        valor = float(input("Ingrese el radio de la esfera: "))
        print("Resultado: ",esfera(valor))
    if opcion == 5:
        print("Salir!")
    if opcion >= 6:
        print("Seleccione una opcion correcta!!")
