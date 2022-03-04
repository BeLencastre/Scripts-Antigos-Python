while True:
    cpf = ' '
    while not cpf.isnumeric() or len(cpf) != 11:
        cpf = str(input('CPF: '))
    cpf_novo = cpf[:-2]

    soma = 0
    reverso = 10

    for index in range(19):
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

    print('\033[1;32mCPF VÁLIDO\033[m') if cpf == cpf_novo else print('\033[1;31mCPF INVÁLIDO\033[m')
