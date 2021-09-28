def tautograma(frase):
    listap = frase.split()

    pl = (listap [0][0]).lower()
    contador = 0
    while contador < len(listap):
        if (listap[contador][0]).lower() != pl:
            return 'N'
        contador += 1
    return 'Y'

palavra = (input())
if len(palavra) > 50:
    print('Erro')
else:
    print(tautograma(palavra))

