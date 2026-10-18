from utilitarios.cores import cor


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


def lerArquivo(nome):
    try:
        with open(nome, 'r') as a:
            lista = a.read()
            if lista.strip() == '':
                print(f'{cor["amarelo"]}A lista de tarefas está vazia.{cor["limpa"]}')
            else:
                print(lista)
    except Exception as erro:
        print(f'{cor["vermelho"]}Não foi possível ler o arquivo. Causa: {erro}{cor["limpa"]}')


def addTarefa(arq, t):
    try:
        with open(arq,'a') as a:
            a.write(f'{t}\n')
    except Exception as erro:
        print(f'{cor["vermelho"]}Não foi possível adicionar a tarefa. Causa: {erro}{cor["limpa"]}')
    else:
        print(f'{cor["verde"]}A tarefa "{t}" foi adicionada com sucesso.{cor["limpa"]}')
