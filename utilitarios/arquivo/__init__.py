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
            print(a.read())
    except Exception as erro:
        print(f'{cor["vermelho"]}Não foi possível ler o arquivo. Causa: {erro}{cor["limpa"]}')