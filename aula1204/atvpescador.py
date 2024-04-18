peso_peixe = int(input('\nDigite quantos kg de peixe voce pegou\n'))
if peso_peixe > 50:
    peso_excedente= peso_peixe - 50
    multa = peso_excedente*4
    print(f'\n\nvoce passou {peso_excedente}kg do peso permitido pelo \nestasbelecimento sua multa eh de {multa},00')