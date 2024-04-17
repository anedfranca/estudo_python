altura = float(input('Digite sua altura: '))
sexo = input('Digite seu genero (f/m): ')

pesoideal_mulher = (62.1*altura)-44.7
pesoideal_homem = (72.7*altura)-58

if sexo == 'f':
    print(f'Seu peso ideal é: {pesoideal_mulher:.0f}f')

else:
    print(f'Seu peso ideal é: {pesoideal_homem:.0f}')

