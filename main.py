from utilitarios.interface import *
from utilitarios.arquivo import *
from utilitarios.cores import cor

arq = 'tarefas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

titulo('GERENCIADOR DE TAREFAS')
while True:
    resp = menu(['Adicionar uma nova tarefa', 'Listar todas as tarefas', 'Sair do programa'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        print('addTarefa')
    elif resp == 3:
        print('Finalizando...')
        break
titulo('VOLTE SEMPRE'.center(50))