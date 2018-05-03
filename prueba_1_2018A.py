#import math

#primer ejercicio calculaladora binaria

print("\t\t\tEsta es una  calculadora binaria ")
print("Se tomara el valor binario de un archivo .txt llamado numero el cual contiene dicho")

binario = open('numero.txt','r')
l = binario.readline()
binario.close()
print("El numero Binario es: ",l)

peso = len(l)
print(peso)
b=0
num=peso-1
suma =0
for n in l:
    num1=int(l[b])*2**num
    num=num-1
    b=b-1
    #print("numro",num1)
    suma=num1+suma


print("El resultado es",suma)
archivo = open('suma.txt', 'a')
archivo.write("Vicente Delgado"+'\n')
archivo.write("El resultado de la suma es: "+'%s'% suma)
archivo.close()



# ejercicio dos

palabra = ['v','i','c','e','n','t','e']
p = int(len(palabra))-1
print(palabra[2])
c = 0
d=palabra
print(d)
print(p)
e=0
while e<p:
    d[c] = palabra[p]
    c = c+1
    p = p-1
    e=e+1
    archivo1 = open('textoinvertido.txt', 'a')
    archivo1.write( d[c])
    archivo1.close()

#ejercicio tres

codigo=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
codificador=[]



