def creartxt():
    archive=open('2.txt','w')
    archive.close()

def grabartxt():
    archive=open('2.txt','a')
    cad = 'Python'
    print(cad)
    cad2 = cad[5]+cad[4]+cad[3]+cad[2]+cad[1]+cad[0]
    archive.write("La cadena es:"+ cad2)

creartxt()
grabartxt()