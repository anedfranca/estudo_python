cont = 0
soma = 0

while True:
    glicose = int(input())
    if glicose == 0:
        break

    cont += 1
    soma += glicose


#Calc media
media = soma/cont
if media < 110:
    print('Glicose Normal')
elif media >= 200:
    print('Glicose Muito Alta')
else:
    print('Glicose Alterada')
        
