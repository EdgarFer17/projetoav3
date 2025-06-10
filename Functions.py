def reservar_carona(email_motorista,data_carona,caronas,usuario_logado):
    carona_encontrada = None
    for carona in caronas:
        if carona['email_motorista'] == email_motorista and carona['data'] == data_carona:
            carona_encontrada = carona
            if carona_encontrada:
                if carona_encontrada['vagas'] > 0:
                    carona_encontrada['vagas'] -= 1
                    carona_encontrada['reservas'].append(usuario_logado['nome'])
                    return carona
        elif carona['email_motorista'] != email_motorista or carona['data'] != data_carona:
            print('o email ou data da carona está errado!')
        else:
            print('Desculpe, essa carona não tem mais vagas disponíveis.')
    if carona_encontrada == None:
        print('Carona não encontrada')

def cadastrar_usuarios(naopode, cadastro, count):
    
    print('Vamos fazer o seu cadastro!')
    nome = input('Escreva seu nome completo: ').strip().lower()
    email = input('Digite um email valido: ').strip().lower()

    while True:
        validacao = True
        for carac in naopode:
            if carac in email:
                validacao = False
                break

        email_existente = False
        for usuario in cadastro:
            if 'email' in usuario and usuario['email'] == email:
                email_existente = True
                break
        
        email_valido = '@gmail.com' in email or '@hotmail.com' in email or '@outlook.com' in email

        if not validacao:
            email = input('Email inválido (contém caracteres proibidos). Digite novamente: ').lower()
        elif email_existente:
            email = input('Este email já está cadastrado. Tente outro: ').lower()
        elif not email_valido:
            email = input('Email inválido. O email deve conter @gmail.com, @hotmail.com ou @outlook.com. Digite novamente: ').lower()
        else:
            break

    senha = input('Crie sua senha: ').strip()

    while True:
        tipo_usuario = input('Você deseja se cadastrar como Motorista ou Usuário? (M/U): ').strip().upper()
        if tipo_usuario in ['M', 'U']:
            break
        else:
            print('Opção inválida. Digite "M" para Motorista ou "U" para Usuário.')

    cadastro.append({
        'ID': count,
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': 'Motorista' if tipo_usuario == 'M' else 'Usuário'
    })
    print('O usuário foi cadastrado com sucesso!')
    with open("usuarios.txt", "w", encoding="utf-8") as edgar:
        edgar.write(f"ID: {count}, Nome: {nome}, Email: {email}, Senha: {senha}\n")

def detalhes_da_carona(email_motorista,data_carona,caronas):

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


def carona_disponiveis(caronas):
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

def cancelar_cadastro(caronas,usuario_logado):
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

def fazer_login(cadastro):
    email_login = input('Digite seu email: ').strip().lower()
    senha_login = input('Digite sua senha: ').strip()

    for cadastrados in cadastro:
        if 'email' in cadastrados and 'senha' in cadastrados:
            if cadastrados['email'] == email_login and cadastrados['senha'] == senha_login:
                print(f"Login realizado com sucesso! Bem-vindo(a), {cadastrados['nome']}.")
                return cadastrados
    print('Email ou senha incorretos.')
    return None


def importar_usuarios():
    usuarios = []
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(", ")
            dados = {}
            for parte in partes:
                chave, valor = parte.split(": ")
                dados[chave.strip()] = valor.strip()
            dados['ID'] = int(dados['ID'])
            usuarios.append(dados)
    return usuarios

def relatorio_totalizador(caronas, usuario_logado):
    print('------ Relatório de Totalizadores ------')
    encontrou = False
    total_geral = 0

    for carona in caronas:
        if carona['email_motorista'] == usuario_logado['email']:
            encontrou = True
            vagas_ocupadas = len(carona['reservas'])
            total_receber = carona['valor_vaga'] * vagas_ocupadas
            total_geral += total_receber
            print('\n--- Carona ---')
            print(f"Origem: {carona['origem']}")
            print(f"Destino: {carona['destino']}")
            print(f"Data: {carona['data']}")
            print(f"Horário: {carona['horario']}")
            print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
            print(f"Vagas restantes: {carona['vagas']}")
            print(f"Total a receber: R$ {total_receber:.2f}")
    
    if not encontrou:
        print("Não há caronas cadastradas.")
    else:
        print('\n----------------------------------------')
        print(f"TOTAL GERAL A RECEBER: R$ {total_geral:.2f}")
