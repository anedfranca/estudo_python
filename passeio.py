voto_cinema = 0
voto_boliche = 0
votos = 0

while True:
    votos += 1
    if votos > 7:
        break

    passeio = input().upper()

    if passeio == 'BOLICHE':
        voto_boliche += 1
    else:
        voto_cinema+= 1

if voto_boliche > voto_cinema:
    print('BOLICHE')
else:
    print('CINEMA')
    
