from utilitarios.cores import cor
from time import sleep


def linha(tam=50):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(msg.center(50))
    print(linha())
    sleep(1)


def menu(lst):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lst:
        if c == 3:
            print(f'{cor["vermelho"]}{c} - {cor["limpa"]}{item}')
        else:
            print(f'{cor["amarelo"]}{c} - {cor["limpa"]}{item}')
            c = c + 1
    sleep(0.5)
    print(linha())
    opc = leiaInt('Sua opção: ')
    sleep(0.5)
    return opc


def leiaInt(opc):
    while True:
        try:
            n = int(input(opc))
        except (ValueError, TypeError):
            print(f'{cor["vermelho"]}Valor inválido, digite um número: {cor["limpa"]}')
        except KeyboardInterrupt:
            print(f'\n{cor["amarelo"]}O usuário interrompeu a ação.{cor["limpa"]}')
            return 3
        else:
            return n