while True:
    cnpj = ' '
    while not cnpj.isnumeric() or len(cnpj) != 14:
        cnpj = str(input('CNPJ: '))
    cpf_novo = cnpj[:-2]
    cnpj_novo = cnpj[:-2]
    soma1 = soma2 = 0
    cont1 = 5
    cont2 = 6

    for c in range(12):
        if cont1 == 1:
            cont1 = 9
        soma1 += int(cnpj_novo[c]) * cont1
        cont1 -= 1

    d = 11 - (soma1 % 11)
    if d > 9:
        d = 0
    cnpj_novo += str(d)

    for c in range(13):
        if cont2 == 1:
            cont2 = 9
        soma2 += int(cnpj_novo[c]) * cont2
        cont2 -= 1

    d = 11 - (soma2 % 11)
    if d > 9:
        d = 0
    cnpj_novo += str(d)

    if cnpj == cnpj_novo:
        print(f'\033[1;32mCNPJ VÁLIDO\033[m')
    else:
        print(f'\033[1;31mCNPJ INVÁLIDO\033[m')
