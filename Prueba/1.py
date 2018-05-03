#prueba_1_2018A
import math
def creartxt():
    archive=open('1.txt','w')
    archive.close()

def grabartxt():
    archive=open('1.txt','a')
    cad = '110101'
    cad2 = (cad[0]*pow(2,5)) + (cad[1]*pow(2,4)) + (cad[2]*pow(2,3)) + (cad[3]*pow(2,2)) + \
           (cad[4]*pow(2,1)) + (cad[5]*pow(2,0))
    resultado=cad2[0]+cad2[1]+cad2[2]+cad2[3]+cad2[4]+cad2[5]
    archive.write(resultado)
    archive.write("\n")
    archive.write('Oscar Mateo Peñaherrera')

creartxt()

grabartxt()
