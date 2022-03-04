from random import randint

print('\033[1;97m{:—^44}\033[m'.format(' ESCOLHA OS LIMITES '))
inicio = int(input('Limite Inicial: '))
fim = int(input('Limite Final:   '))

dica = ' '
while dica not in 'SN':
    dica = str(input('Você quer receber dicas? [S/N] ')).upper().strip()[0]

tentativas = 1
jogadas = []
random = randint(inicio, fim)

print('\n\033[1;97m{:—^44}\033[m'.format(' ADIVINHE O NÚMERO SORTEADO '))
player = int(input(f'Escolha um número entre {inicio} e {fim}: '))

while player != random:
    jogadas.append(player)
    tentativas += 1

    if dica == 'S':
        if player < random:
            print('\033[31mMAIS...\033[m TENTE NOVAMENTE.')
        else:
            print('\033[31mMENOS...\033[m TENTE NOVAMENTE.')

    elif dica == 'N':
        print('\033[31mNÚMERO ERRADO.\033[m TENTE NOVAMENTE.')
    player = int(input('Escolha outro número: '))

jogadas.append(player)
print('\033[32mPARABÉNS!!! VOCÊ ACERTOU!\033[m')

print('—' * 40)
print(f'Número sorteado: \033[1m{random}\033[m')
print(f'Jogadas: {jogadas}')
print(f'Tentativas: \033[1m{tentativas}\033[m')
