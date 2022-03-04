from random import randint

cont = int(input('Quantos CPFs serão gerados? '))
print('—' * 30)
for c in range(cont):
    num = str(randint(100000000, 999999999))
    cpf_novo = num

    soma = 0
    reverso = 10

    for index in range(19):  # Repetir 19 vezes
        if index > 8:
            index -= 9

        soma += int(cpf_novo[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (soma % 11)
            if d > 9:
                d = 0
            soma = 0
            cpf_novo += str(d)

    print(cpf_novo)
