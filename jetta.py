soma = 0

for i in range(7):
    valor = float(input())

    if i != 0: # nao for a primeira iteracao
        print(valor, dia_anterior)


    dia_anterior = valor

    # iguaisssssssssss



    soma += valor

print(f'R$ {soma:.2f}')