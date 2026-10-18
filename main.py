from utilitarios.interface import *
from utilitarios.arquivo import *
from utilitarios.cores import cor


arq = 'tarefa.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

titulo('GERENCIADOR DE TAREFAS')

while True:
    resp = menu(['Adicionar uma tarefa', 'Listar todas as tarefas', 'Sair do programa'])
    if resp == 1:
        titulo('ADICIONAR TAREFA')
        while True:
            try:
                t = str(input('Adicione uma tarefa: '))
                if t.strip() == '':
                    print(f'{cor["vermelho"]}Erro! A tarefa não pode estar vazia.{cor["limpa"]}')
                    continue

                if t.isnumeric():
                    print(f'{cor["vermelho"]}Erro! A tarefa é inválida.{cor["limpa"]}')
                    continue

            except KeyboardInterrupt:
                print(f'\n{cor["amarelo"]}O usuário interrompeu a ação.{cor["limpa"]}')
                break

            else:
                addTarefa(arq, t) 
                break 
        

    elif resp == 2:
        lerArquivo(arq)

    elif resp == 3:
        print(f'{cor["vermelho"]}Finalizando...{cor["limpa"]}')
        break
    else:
        print(f'{cor["vermelho"]}Erro! Digite uma das opções do menu.{cor["limpa"]}')

print(cor["vermelho"])
titulo('VOLTE SEMPRE!')
print(cor["limpa"])