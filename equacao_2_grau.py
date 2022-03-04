def linha():
    print('—' * 46)


def inicio():
    linha()
    print(f'{"CALCULADORA DE EQUAÇÕES DE 2º GRAU":^46}')
    print(f'{"FORMATO: ax² + bx + c":^46}')
    linha()


def inserir():
    print('Insira os valores das variáveis abaixo')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    linha()
    delta = (b ** 2) - (4 * a * c)
    print('Δ = b² - 4ac')
    print(f'Δ = {b ** 2} - 4 * {a * c}')
    print(f'Δ = {b ** 2} - {4 * (a * c)}')
    print(f'Δ = {(b ** 2) - (4 * a * c)}')

    if delta < 0:
        print('DELTA NEGATIVO! RAÍZES NÃO REAIS.')

    elif delta == 0:
        print('DELTA ZERO! DUAS RAÍZES REAIS E IGUAIS.')
        linha()
        raiz = (-b + 0) / (2 * a)
        print('r = -b ÷ 2a')
        print(f'r = {-b} ÷ 2 * {a}')
        print(f'r = {-b} ÷ {2 * a}')
        print(f'r = {(-b) / (2 * a)}')

    elif delta > 0:
        print('DELTA POSITIVO! DUAS RAÍZES REAIS E DISTINTAS.')
        linha()

        raizd = round(pow(delta, 1/2), 2)

        raiz1 = round((-b + raizd) / (2*a), 2)
        print(f'r₁ = ({-b} + √{delta}) ÷ (2 * {a})')
        print(f'r₁ = ({-b} + {raizd}) ÷ {2*a}')
        print(f'r₁ = {round((-b) + raizd, 2)} ÷ {2*a}')
        print(f'r₁ = {round((-b + raizd) / (2*a), 2)}')

        linha()

        raiz2 = round((-b - raizd) / (2*a), 2)
        print(f'r₂ = ({-b} - √{delta}) ÷ (2 * {a})')
        print(f'r₂ = ({-b} - {raizd}) ÷ {2*a}')
        print(f'r₂ = {round((-b) - raizd, 2)} ÷ {2*a}')
        print(f'r₂ = {round((-b - raizd) / (2*a), 2)}')

        linha()

        print(f'As raízes são: {raiz1} e {raiz2}')


def finalizar():
    linha()
    print('\033[1;31mPROGRAMA ENCERRADO. VOLTE SEMPRE!')


inicio()
inserir()
finalizar()