from Functions import *
cadastro = []
naopode = '!#$%¨&*()-_+=[]'
autenticado = False
usuario_logado = None
caronas = []
count = 0


while True:
    print('----------------             BABLACAR         -------------')
    print('----------------  [1] Cadastrar Novo Usuario  -------------')
    print('----------------  [2]         Login           -------------')
    print('----------------  [3]          Sair           -------------')
    op = input('Digite uma das opções acima: ')

    if op in ['1', '2', '3']:
        op = int(op)
    else:
        print("Por favor, digite apenas 1, 2 ou 3.")

    if op == 1:
        count += 1
        cadastrar_usuarios(naopode, cadastro,count )
        

    elif op == 2:
        print('-------- Login --------')
        email_login = input('Digite seu email: ').strip().lower()
        senha_login = input('Digite sua senha: ').strip()
        for cadastrados in cadastro:
            if cadastrados['email'] == email_login and cadastrados['senha'] == senha_login:
                autenticado = True
                usuario_logado = cadastrados
                print(f"Login bem-sucedido! Bem-vindo(a), {cadastrados['nome']} ({cadastrados['tipo']}).")

                while True:
                    print('\n------------------- Menu de Caronas -------------------')
                    if usuario_logado['tipo'] == 'Motorista':
                        print('[1] Cadastrar Carona')
                        print('[2] Ver Caronas Disponíveis')
                        print('[3] Buscar Carona')
                        print('[4] Reservar Vaga em Carona')
                        print('[5] Voltar')
                        print('[6] Cancelar cadastro de carona')
                        print('[7] Mostrar Detalhes de Carona')
                        print('[8] Mostrar Caronas Cadastradas')
                        print('[9] Trocar senha da conta')
                    else:
                        print('[1] Ver Caronas Disponíveis')
                        print('[2] Buscar Carona')
                        print('[3] Reservar Vaga em Carona')
                        print('[4] Voltar')
                        print('[5] Cancelar reserva')
                        print('[6] Mostrar Detalhes de Carona')
                        print('[7] Trocar senha da conta')

                    op_menu = int(input('Escolha uma opção: '))

                    if usuario_logado['tipo'] == 'Motorista':
                        if op_menu == 1:
                            print(f'Cadastro de carona ---- {usuario_logado["nome"]} ----')
                            origem = input('Digite o local de origem: ').strip()
                            destino = input('Digite o destino: ').strip()
                            data = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()
                            horario = input('Digite o horário da carona (ex: HH:MM): ').strip()
                            vagas = int(input('Digite a quantidade de vagas: ').strip())
                            valor_vaga = float(input('Digite o valor por vaga: ').strip())

                            carona = {
                                'motorista': usuario_logado['nome'],
                                'email_motorista': usuario_logado['email'],
                                'origem': origem,
                                'destino': destino,
                                'data': data,
                                'horario': horario,
                                'vagas': vagas,
                                'valor_vaga': valor_vaga,
                                'reservas': []
                            }
                            caronas.append(carona)
                            print('Carona cadastrada com sucesso!')

                        elif op_menu == 2:
                            print('------ Caronas Disponíveis ------')
                            caronas_disponiveis = []
                            for c in caronas:
                                if c['vagas'] > 0:
                                    caronas_disponiveis.append(c)
                            if len(caronas_disponiveis) == 0:
                                print('Nenhuma carona disponível no momento.')
                            else:
                                for carona in caronas_disponiveis:
                                    print("\n--- Carona ---")
                                    print(f"Motorista: {carona['motorista']}")
                                    print(f"Origem: {carona['origem']}")
                                    print(f"Destino: {carona['destino']}")
                                    print(f"Data: {carona['data']}")
                                    print(f"Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['vagas']}")
                                    print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")


                        elif op_menu == 3:
                            print('------  MENU DE BUSCA  ------')
                            busca_origem = input('Digite a origem desejada: ').lower()
                            busca_destino = input('Digite o destino desejado: ').lower()

                            caronas_disponiveis = []
                            for c in caronas:
                                if c['vagas'] > 0:
                                    caronas_disponiveis.append(c)
                            encontrou = False
                            for carona in caronas_disponiveis:
                                if carona['origem'].lower() == busca_origem and carona['destino'].lower() == busca_destino:
                                    print("\n--- Carona Encontrada ---")
                                    print(f"Motorista: {carona['motorista']}")
                                    print(f"Origem: {carona['origem']}")
                                    print(f"Destino: {carona['destino']}")
                                    print(f"Data: {carona['data']}")
                                    print(f"Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['vagas']}")
                                    print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                    encontrou = True
                            if not encontrou:
                                print('Nenhuma carona encontrada.')

                        elif op_menu == 4:
                            print('------ Reservar Vaga em Carona ------')
                            email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                            data_carona = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()

                            carona_encontrada = verificar_carona(email_motorista,data_carona,caronas,usuario_logado)
                            if carona_encontrada:
                                print('Reseva feita com sucesso!')
                                
                           

                        elif op_menu == 5:
                            print('Voltando ao menu principal...')
                            break

                        elif op_menu == 6:
                            print('----- CANCELAR CADASTRO -----')

                            tem_carona = False
                            for c in caronas:
                                if c['email_motorista'] == usuario_logado['email']:
                                    tem_carona = True
                                    break

                            if not tem_carona:
                                print('Você não tem caronas cadastradas.')
                            else:
                                data = input('Digite a DATA da carona que deseja cancelar (DD/MM/AAAA): ')

                                encontrou = False
                                for c in caronas:
                                    if c['email_motorista'] == usuario_logado['email'] and c['data'] == data:
                                        encontrou = True
                                        confirmacao1 = input(f'Tem certeza que deseja cancelar a carona? S/N:').upper()
                                        if confirmacao1 == 'S':
                                            caronas.remove(c)
                                            print('Carona cancelada com sucesso!')
                                        else:
                                            print('Você cancelou o cancelamento da sua carona')
                                        break

                                if not encontrou:
                                    print('Nenhuma carona encontrada nesta data!')

                        elif op_menu == 7:
                            print('------ Detalhes da Carona ------')
                            email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                            data_carona = input('Digite a data da carona (DD/MM/AAAA): ').strip()

                            carona_encontrada = detalhes_da_carona(email_motorista,data_carona,caronas)

                        elif op_menu == 8:
                            print ('------ Mostrar Caronas Cadastradas ------')
                            caronas_disponiveis1 = []
                            for c in caronas:
                                if c['vagas'] > 0:
                                    caronas_disponiveis1.append(c)
                            if len(caronas_disponiveis1) == 0:
                                print('Nenhuma carona disponível no momento.')
                            else:
                                for carona in caronas_disponiveis1:
                                    print("\n--- Carona ---")
                                    print(f"Motorista: {carona['motorista']}")
                                    print(f"Origem: {carona['origem']}")
                                    print(f"Destino: {carona['destino']}")
                                    print(f"Data: {carona['data']}")
                                    print(f"Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['vagas']}")
                                    print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                    print(f"Passageiros: {carona['reservas']}")

                        elif op_menu == 9:
                            print('------ Alterar Senha ------')
                            senha_atual = input('Digite sua senha atual: ').strip()
                            if usuario_logado['senha'] == senha_atual:
                                nova_senha = input('Digite a nova senha: ').strip()
                                usuario_logado['senha'] = nova_senha
                                print("Senha alterada com sucesso!")
                            else:
                                print("Senha atual incorreta.")

                    else:

                        if op_menu == 1:
                            print('------ Caronas Disponíveis ------')
                            caronas_disponiveis = []
                            for c in caronas:
                                if c['vagas'] > 0:
                                    caronas_disponiveis.append(c)
                            if len(caronas_disponiveis) == 0:
                                print('Nenhuma carona disponível no momento.')
                            else:
                                for carona in caronas_disponiveis:
                                    print("\n--- Carona ---")
                                    print(f"Motorista: {carona['motorista']}")
                                    print(f"Origem: {carona['origem']}")
                                    print(f"Destino: {carona['destino']}")
                                    print(f"Data: {carona['data']}")
                                    print(f"Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['vagas']}")
                                    print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")


                        elif op_menu == 2:
                            print('------  MENU DE BUSCA  ------')
                            busca_origem = input('Digite a origem desejada: ').lower()
                            busca_destino = input('Digite o destino desejado: ').lower()

                            caronas_disponiveis = []
                            for c in caronas:
                                if c['vagas'] > 0:
                                    caronas_disponiveis.append(c)
                            encontrou = False
                            for carona in caronas_disponiveis:
                                if carona['origem'].lower() == busca_origem and carona[
                                    'destino'].lower() == busca_destino:
                                    print("\n--- Carona Encontrada ---")
                                    print(f"Motorista: {carona['motorista']}")
                                    print(f"Origem: {carona['origem']}")
                                    print(f"Destino: {carona['destino']}")
                                    print(f"Data: {carona['data']}")
                                    print(f"Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['vagas']}")
                                    print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                    encontrou = True
                            if not encontrou:
                                print('Nenhuma carona encontrada.')

                        elif op_menu == 3:
                            print('------ Reservar Vaga em Carona ------')
                            email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                            data_carona = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()

                            carona_encontrada = None
                            for carona in caronas:
                                if carona['email_motorista'] == email_motorista and carona['data'] == data_carona:
                                    carona_encontrada = carona
                                    break

                            if carona_encontrada:
                                if carona_encontrada['vagas'] > 0:
                                    carona_encontrada['vagas'] -= 1
                                    carona_encontrada['reservas'].append(usuario_logado['nome'])
                                    print(f'Parabéns! Você reservou sua vaga com {carona_encontrada["motorista"]}.')
                                else:
                                    print('Desculpe, essa carona não tem mais vagas disponíveis.')
                            else:
                                print('Carona não encontrada.')

                        elif op_menu == 4:
                            print('Voltando ao menu principal...')
                            break

                        elif op_menu == 5:
                            print('------ Cancelar Reserva ------')
                            email = input('E-mail do motorista: ').lower()
                            data = input('Data da carona (DD/MM/AAAA): ')
                            confirmacao = input('Tem certeza que deseja cancelar esta reserva? (S/N): ').upper()
                            if confirmacao == 'S':
                                reserva_encontrada = False
                                for carona in caronas:
                                    if carona['email_motorista'] == email and carona['data'] == data and usuario_logado[
                                        'nome'] in carona['reservas']:
                                        reserva_encontrada = True
                                        carona['reservas'].remove(usuario_logado['nome'])
                                        carona['vagas'] += 1
                                        print('Reserva cancelada com sucesso!')
                                        break
                                if not reserva_encontrada:
                                    print('Reserva não encontrada.')
                            else:
                                print('Operação cancelada pelo usuário.')

                        elif op_menu == 6:
                            print('------ Detalhes da Carona ------')
                            email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                            data_carona = input('Digite a data da carona (DD/MM/AAAA): ').strip()

                            carona_encontrada = None
                            for carona in caronas:
                                if carona['email_motorista'] == email_motorista and carona['data'] == data_carona:
                                    carona_encontrada = carona
                                    break

                            if carona_encontrada:
                                print(f"Origem: {carona_encontrada['origem']}")
                                print(f"Destino: {carona_encontrada['destino']}")
                                print(f"Horário: {carona_encontrada['horario']}")
                                print(f"Valor por vaga: R$ {carona_encontrada['valor_vaga']:.2f}")
                                print(f"Vagas restantes: {carona_encontrada['vagas']}")

                                if len(carona_encontrada['reservas']) > 0:
                                    passageiros = ""
                                    for i in range(len(carona_encontrada['reservas'])):
                                        if i < len(carona_encontrada['reservas']) - 1:
                                            passageiros += carona_encontrada['reservas'][i] + ", "
                                        else:
                                            passageiros += carona_encontrada['reservas'][i]
                                    print(f"Passageiros: {passageiros}")
                                else:
                                    print("Sem passageiros reservados.")
                            else:
                                print("Carona não encontrada.")

                        elif op_menu == 7:
                            print('------ Alterar Senha ------')
                            senha_atual = input('Digite sua senha atual: ').strip()
                            if usuario_logado['senha'] == senha_atual:
                                nova_senha = input('Digite a nova senha: ').strip()
                                usuario_logado['senha'] = nova_senha
                                print("Senha alterada com sucesso!")
                            else:
                                print("Senha atual incorreta.")

    elif op == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")



















