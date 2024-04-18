cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while True: 
    numero = int(input('Digite um numero '))

    if numero<0:
        break
    
    if numero >= 0 and numero <= 25:
        cont1+=1 

    if numero >= 26 and numero <= 50:
        cont2+=1 

    if numero >= 51 and numero <= 75:
        cont3+=1 

    if numero >= 76 and numero <= 100:
        cont4+=1 

print (cont1, cont2, cont3, cont4)