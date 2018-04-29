print("PRUEBA 1")
print("Seleccione una figura")
print("1. Cubo")
print("2. ")
print("3. ")

def cubo():
    lado=float(input("Ingrese el lado del cubo"))
    lado=lado*lado*lado
    print ("El volumen del cubo es: ",lado)

def func2():
    print ("Func2")

def func3():
    print("FuncN")

def defaultFunc():
    print ("ERROR")

opcion=int(input("Seleccione una opcion"))
if(opcion==1):
    cubo()
if(opcion==2):
    func2()
if(opcion==3):
    func3()
if(opcion>3):
    defaultFunc()