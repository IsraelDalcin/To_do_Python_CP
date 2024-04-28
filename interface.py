from crud_list import TarefaComListaDao
import os
from time import sleep

print('Seja bem vindo ao nosso TO-DO list!')
print('-='*18)

tarefa_dao = TarefaComListaDao()

# Função main do programa
def main():
    while True:
        verifica_status = input('Digite o que você deseja realizar\n[1] para inserir uma tarefa\n[2] para selecionar\n[3] para atualizar alguma tarefa\n[4] para remover uma tarefa\n[5] caso queira sair do programa: ')

        # Verificando se foi digitado no intervalo do programa
        while verifica_status != '1' and verifica_status != '2' and verifica_status != '3' and verifica_status != '4' and verifica_status != '5':
            os.system('cls')
            print('ERRO!')
            print('Digite um número entre 1 e 5 para escolher uma funcionalidade.')
            verifica_status = input('Digite o que você deseja realizar\n[1] para inserir uma tarefa\n[2] para selecionar\n[3] para atualizar alguma tarefa\n[4] para remover uma tarefa\n[5] caso queira sair do programa: ')
        
        # Saindo do programa
        if verifica_status == '5':
            print()
            print('Saindo do programa...')
            break

        # Insert
        if verifica_status == '1':
            os.system('cls')
            print('Você selecionou inserir uma tarefa!')
            print('-='*18)
            titulo_tarefa = input('Digite qual será o título da tarefa: ').lower().strip()
            descricao_tarefa = input('Digite a descrição desta tarefa: ')
            data_venc_tarefa = input('Digite a data de vencimento da tarefa: ')
            tarefa_dao.insert(titulo_tarefa, descricao_tarefa, data_venc_tarefa)
            os.system('cls')
            print('Tarefa inserida com sucesso!')
        
        # Select
        if verifica_status == '2':
            os.system('cls')
            print('Você selecionou a opção de selecionar uma tarefa!')
            print('-='*25)
            print('Todas as tarefas listadas até o momento: ')
            for tarefa in tarefa_dao.selectAll():
                print(f'{tarefa.id_tarefa} - {tarefa.titulo}')
            verifica_busca_tarefa = input('Você deseja buscar uma tarefa específica? (S / N): ').lower().strip()

            while verifica_busca_tarefa != 's' and verifica_busca_tarefa != 'n':
                print('ERRO!')
                verifica_busca_tarefa = input('Digite um valor entre S / N: ').lower().strip()
            if verifica_busca_tarefa in 'Ss':
                os.system('cls')
                print('Todas os títulos das tarefas listadas até o momento: ')
                for tarefa in tarefa_dao.selectAll():
                    print(f'{tarefa.id_tarefa} - {tarefa.titulo}')
                
                verifica_tipo = input('Digite [1] para buscar por status | Digite [2] para buscar por data de vencimento: ')

                while verifica_tipo != '1' and verifica_tipo != '2':
                    print('Erro! Digte 1 ou 2')
                    verifica_tipo = input('Digite [1] para buscar por status | Digite [2] para buscar por data de vencimento: ')

                if verifica_tipo == '1':
                    verifica_condicional_id = True
                    while verifica_condicional_id:
                        status_busca = input('Digite o status da tarefa você deseja buscar [Pendente] [Em andamento] [Concluído]: ').lower().strip()
                        if status_busca == 'em andamento' or status_busca == 'pendente' or status_busca == 'concluído':
                            os.system('cls')
                            for tarefa in tarefa_dao.selectAll():
                                if status_busca.lower().strip() == tarefa.status.lower().strip():
                                    print(tarefa)
                                    verifica_condicional_id = False
                            if verifica_condicional_id == False:
                                break
                            else:
                                print(f'ERRO! Não encontramos nenhuma tarefa com o status {status_busca}')
                        else:
                            print('ERRO! Digite um valor entre [Pendente] [Em andamento] [Concluído]!')
                    print('\n')
                else:
                    verifica_condicional_id = True
                    while verifica_condicional_id:
                        status_busca_datavec = input('Digite a data de vencimento da tarefa você deseja buscar: ').strip()
                        os.system('cls')
                        for tarefa in tarefa_dao.selectAll():
                            if status_busca_datavec.strip() == tarefa.data_venc_tarefa.strip():
                                print(tarefa)
                                verifica_condicional_id = False
                        if verifica_condicional_id == False:
                            break
                        else:
                            print(f'ERRO! Não encontramos nenhuma tarefa com essa data de vencimento"{status_busca_datavec}')

                    print('\n')
            else:
                os.system('cls')

        #Update
        if verifica_status == '3':
            os.system('cls')
            print('Você selecionou a opção de atualizar uma tarefa!')
            print('-='*25)
            print('Estas são todas as tarefas listadas!')
            for tarefa in tarefa_dao.selectAll():
                print(tarefa)
            verifica_condicional_id = True
            while verifica_condicional_id:
                    id_busca = input('Digite o id da tarefa você deseja atualizar: ')
                    if id_busca.isdigit():
                        for tarefa in tarefa_dao.selectAll():
                            if int(id_busca) == tarefa.id_tarefa:
                                os.system('cls')
                                verifica_status_update = input('Digite o que você deseja realizar\n[1] para atualizar o título\n[2] para atualizar a descrição\n[3] para atualizar a data do prazo\n[4] atualizar o status da tarefa\n[5] para atualizar todos os itens da tarefa: ')
                                # Temos algumas condições pra saber se o usuário quer alterar algum atributo específico
                                while verifica_status_update != '1' and verifica_status_update != '2' and verifica_status_update != '3' and verifica_status_update != '4' and verifica_status_update != '5':
                                    os.system('cls')
                                    print('ERRO!')
                                    print('Digite um número entre 1 e 5 para escolher uma funcionalidade.')
                                    verifica_status_update = input('Digite o que você deseja realizar\n[1] para atualizar o título\n[2] para atualizar a descrição\n[3] para atualizar a data do prazo\n[4] atualizar o status da tarefa\n[5] para atualizar todos os itens da tarefa: ')
                                if verifica_status_update == '1':
                                    print(tarefa_dao.select_by_name(id_busca))
                                    titulo_tarefa_update = input('Digite qual será o novo título da tarefa: ').lower().strip()
                                    tarefa_dao.update_unico(int(id_busca), titulo = titulo_tarefa_update)
                                elif verifica_status_update == '2':
                                    print(tarefa_dao.select_by_name(id_busca))
                                    descricao_tarefa_update = input('Digite a nova descrição desta tarefa: ')
                                    tarefa_dao.update_unico(int(id_busca), descricao= descricao_tarefa_update)
                                elif verifica_status_update == '3':
                                    print(tarefa_dao.select_by_name(id_busca))
                                    data_venc_tarefa_update = input('Digite a nova data de vencimento da tarefa: ')
                                    tarefa_dao.update_unico(int(id_busca), data_venc_tarefa= data_venc_tarefa_update)
                                elif verifica_status_update == '4':
                                    print(tarefa_dao.select_by_name(id_busca))
                                    status_update = input('Digite o novo status da tarefa [Pendente / Em andamento / Concluído]: ')
                                    tarefa_dao.update_unico(int(id_busca), status= status_update)
                                else:
                                    print(tarefa_dao.select_by_name(id_busca))
                                    titulo_tarefa_update = input('Digite qual será o novo título da tarefa: ').lower().strip()
                                    descricao_tarefa_update = input('Digite a nova descrição desta tarefa: ')
                                    data_venc_tarefa_update = input('Digite a nova data de vencimento da tarefa: ')
                                    status_update = input('Digite o novo status da tarefa [Pendente / Em andamento / Concluído]: ')
                                    tarefa_dao.update(int(id_busca), titulo_tarefa_update, descricao_tarefa_update, data_venc_tarefa_update, status_update)
                                verifica_condicional_id = False
                        if verifica_condicional_id == False:
                            break
                        else:
                            print('ERRO! Id não encontrado')
                    else:
                        print('ERRO! Digite apenas números!')
            os.system('cls')
            print("Tarefa atualizada com sucesso!")
            print(tarefa_dao.select_by_name(id_busca))
            print('\n')

        #Delete
        if verifica_status == '4':
            os.system('cls')
            print('Você selecionou a opção de remover uma tarefa!')
            print('-='*25)
            print('Estas são todas as tarefas listadas!')
            for tarefa in tarefa_dao.selectAll():
                print(tarefa)
            verifica_condicional_id = True
            while verifica_condicional_id:
                id_busca_remover = input('Digite o id da tarefa você deseja remover: ')
                if id_busca_remover.isdigit():
                    for tarefa in tarefa_dao.selectAll():
                        if int(id_busca_remover) == tarefa.id_tarefa:
                            tarefa_dao.delete(id_busca_remover)
                            verifica_condicional_id = False
                else:
                    print('ERRO! Digite apenas números.')

            #os.system('cls')
            print(f"Tarefa removida com sucesso!")
            for tarefa in tarefa_dao.selectAll():
                print(tarefa)

# Precisamos dessa linha de código para que o programa não resete o counter do id cada vez que o programa é executado
try:
    lista_tarefas = tarefa_dao.selectAll()
    ultimo_elemento = lista_tarefas[len(lista_tarefas)-1]
    tarefa_dao.troca_id(ultimo_elemento.id_tarefa)
    main()
except:
    main()