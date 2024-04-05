from random import choice

lista_palpites =[]
lista_palavras = []


#escolhe uma palavra aleatoria
with open("palavras.txt", "r") as arquivo:
    for palavra in arquivo:
        lista_palavras.append(palavra.strip()) # Limpa os caracteres em branco e as quebras de linha

palavra_escolhida = choice(lista_palavras)

#########################################################

#criptografa a palavra
print("\nSua palavra: ", end=" ")
numero_letras = (len(palavra_escolhida))
for i in range (numero_letras):
    print('_', end=' ')

print()

#########################################################
#pede ao jogador uma letra e adiciona ela na lista

contador_erros = 0
while True:
    if (contador_erros == 6):
        break

    palpite = input('\nDigite uma letra: ')

    # Validar o meu palpite
    if (palpite not in lista_palpites):
        print("valido")
    if (len(palpite) == 1):
        print("valido")


    lista_palpites.append(palpite)
    lista_palpites.sort()

    # printa a palavra criptografada
    print()
    for letra in palavra_escolhida:
        if letra in lista_palpites:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
    print("\n")


    ##############################################################
    # printa a forca correta
    if (palpite not in palavra_escolhida): # se a letra nao esta na palavra
        contador_erros += 1
    else:
        print("acertou!!!")
    with open(f"sprites/sprite{contador_erros}.txt", "r") as forca:
        for i in forca:
            print(i, end="")
    print("\n")

    # Mostra os chutes já realizados
    print("\nChutes realizados: ", end="| ")
    for chute in lista_palpites:
        print(f"{chute} | ", end='')


print(f'Fim de jogo, a palavra era: {palavra_escolhida}')




