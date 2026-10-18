from utilitarios.cores import cor
from utilitarios.interface import titulo, linha


def arquivoExiste(nome):
    try:
        with open(nome, 'r') as a:
            pass        
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        with open(nome, 'w+') as a:
            pass
    except Exception as erro:
        print(f'{cor["vermelho"]}Ocorreu um erro ao criar o arquivo. Causa: {erro}{cor["limpa"]}')


def lerArquivo(nome, encoding='utf-8'):
    try:
        with open(nome, 'r') as a:
            linhas = a.readlines()
            if not linhas:
                print(f'{cor["amarelo"]}A lista de tarefas está vazia.{cor["limpa"]}')
            else:
                print(f'{cor["amarelo"]}')
                titulo('LISTA DE TAREFAS')
                print(f'{cor["limpa"]}')
                for pos, tarefa in enumerate(linhas, 1):
                    print(f'{cor["amarelo"]}{pos}{cor["limpa"]} - {tarefa.strip()}')
                
                print(f'{cor["amarelo"]}')
                print(linha())
                print(f'{cor["limpa"]}', end='')

    except Exception as erro:
        print(f'{cor["vermelho"]}Não foi possível ler o arquivo. Causa: {erro}{cor["limpa"]}')


def addTarefa(arq, t, encoding='utf-8'):
    try:
        with open(arq,'a') as a:
            a.write(f'{t}\n')
    except Exception as erro:
        print(f'{cor["vermelho"]}Não foi possível adicionar a tarefa. Causa: {erro}{cor["limpa"]}')
    else:
        print(f'{cor["verde"]}A tarefa "{t}" foi adicionada com sucesso.{cor["limpa"]}')
