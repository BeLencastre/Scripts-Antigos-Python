from random import randint
from time import sleep

cor = {'neg': '\033[1m', 'red': '\033[31m', 'gre': '\033[32m', 'yel': '\033[33m', 'blu': '\033[34m'}
emoji = [f'{cor["yel"]}✊\033[m', f'{cor["yel"]}✋\033[m', f'{cor["yel"]}✌\033[m']
itens = (f'PEDRA {emoji[0]}', f'PAPEL {emoji[1]}', f'TESOURA {emoji[2]}')

wins = 0

while True:
    print(f'{cor["neg"]}{" JOKEMPO GAME ":—^26}\033[m')
    print(f'Suas opções:\n[ 0 ] {itens[0]}\n[ 1 ] {itens[1]}\n[ 2 ] {itens[2]}')

    pc = randint(0, 2)
    player = -1
    while not 0 <= player < 3:
        player = int(input('Qual é a sua jogada? '))

    print('—' * 26)
    print('JO', end=' ')
    sleep(1)
    print(f'{"KEN":^19}', end=' ')
    sleep(1)
    print('PO!')
    print('—' * 26)

    print(f'Computador jogou {cor["neg"]}{itens[pc]}\033[m')
    print(f'Jogador    jogou {cor["neg"]}{itens[player]}\033[m')
    print('—' * 26)

    if player == pc:
        print(f'{cor["blu"]}EMPATE!\033[m')

    elif player == 0 and pc == 1:
        print(f'{cor["red"]}DERROTA!\033[m')
        break
    elif player == 0 and pc == 2:
        print(f'{cor["gre"]}VITÓRIA!\033[m')
        wins += 1

    elif player == 1 and pc == 0:
        print(f'{cor["gre"]}VITÓRIA!\033[m')
        wins += 1
    elif player == 1 and pc == 2:
        print(f'{cor["red"]}DERROTA!\033[m')
        break

    elif player == 2 and pc == 0:
        print(f'{cor["red"]}DERROTA!\033[m')
        break
    elif player == 2 and pc == 1:
        print(f'{cor["gre"]}VITÓRIA!\033[m')
        wins += 1

    quer = ' '
    while quer not in 'SN':
        quer = str(input('Quer jogar novamente? [S/N] ')).strip().upper()
    if quer == 'N':
        break
    else:
        print()

print('—' * 26)
print(f'VOCÊ OBTEVE {wins} VITÓRIAS INVICTO.\n{cor["gre"]}PARABÉNS PELO JOGO!!!')
