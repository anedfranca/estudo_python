from random import choice

lista_palpites =[]
lista_palavras = []


#escolhe uma palavra aleatoria
with open("palavras.txt", "r") as arquivo:
    for palavra in arquivo:
        lista_palavras.append(palavra.strip()) # Limpa os caracteres em branco e as quebras de linha

palavra_escolhida = choice(lista_palavras)
print (palavra_escolhida)

#########################################################

#criptografa a palavra
numero_letras = (len(palavra_escolhida))
for i in range (numero_letras):
    print('_', end=' ')

print()

#########################################################
#pede ao jogador uma letra e adiciona ela na lista

contador_erros = 0
while True:
    palpite = input('Digite uma letra: ')
    lista_palpites.append(palpite)
    print(lista_palpites)


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







