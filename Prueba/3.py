def creartxt():
    archive=open('3.txt','w')
    archive.close()

def grabartxt():
    archive=open('3.txt','a')
    a = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L',
         'C', 'K', 'E']
    b=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
    posicion=0;
    cadena1 = ['H','O','L','A']
    while(posicion<=22):
        if cadena1[posicion]==b[posicion]:
            a[posicion]=b[posicion]
            posicion+1
    cad2=[cadena1]
    archive.write("MENSAJE OCULTO:"+cad2)

creartxt()
grabartxt()