while True:
    ph = float(input())

    if ph == -1:
        break

    if ph == 7:
        print('NEUTRA')
    elif ph < 7:
        print('ACIDA')
    else:
        print('BASICA')
