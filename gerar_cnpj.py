from random import randint

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def gerar():
    primeiro_d = randint(0, 9)
    segundo_d = randint(0, 9)
    segundo_b = randint(100, 999)
    terceiro_b = randint(100, 999)
    quarto_b = '0001'
    inicio = f'{primeiro_d}{segundo_d}{segundo_b}{terceiro_b}{quarto_b}00'

    novo_cnpj = calcular(cnpj=inicio, digito=1)
    novo_cnpj = calcular(cnpj=novo_cnpj, digito=2)

    return novo_cnpj

def calcular(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for i, v in enumerate(regressivos):
        total += int(cnpj[i]) * v

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

def formatar(cnpj):
    # cnpj = numeros(cnpj)
    form_cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{12:}'
    return form_cnpj


c = int(input('Quantos CNPJs serão gerados? '))
for i in range(c):
    novo_cnpj = gerar()
    form_cnpj = formatar(novo_cnpj)
    print(form_cnpj)
