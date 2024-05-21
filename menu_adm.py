import os, time, main
import json
import models.usuarios_model as usuario
import models.reservas_model as reservas
import models.condominio_model as condominio
import models.comunicados_model as comunicados

def menuAdm():
    os.system('cls')
    print("="*21)
    print(" MENU DE ADMINISTRADOR ")
    print("="*21)
    
    print("1. Gerenciar usuários") # CRUD USUÁRIOS
    print("2. Gerenciar condomínios") # CRUD Condomínios
    print("3. Gerenciar reservas") # CRUD Reservas
    print("4. Chats de comunicação") # CRUD Comunicação
    print("0. Logout")
    print("10. Sair do sistema")
    
def menuGerenciarUsuario():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR USUÁRIOS ")
    print("="*21)
    
    print("1. Cadastrar um usuário") 
    print("2. Listar usuários") 
    print("3. Atualizar um usuário")  
    print("4. Deletar um usuário") 
    print("0. Voltar ao menu de administrador")
    print("10. Sair do sistema")
    
def menuGerenciarCondominio():
    os.system('cls')
    print("="*21)
    print(" Gerenciar Condominio ")
    print("="*21)

    print("1. Cadastrar condomínio") 
    print("2. Listar condomínio") 
    print("3. Atualizar condomínio")  
    print("4. Deletar condomínio") 
    print("5. Sair")
 
def choiceAdm():
    menuAdm()
    opc = str(input("Digite a opção: "))
    match(opc):
        
        # GERENCIAR USUÁRIOS
        case 1:  
            menuGerenciarUsuario()
            opcao = int(input("Digite uma opção: "))
            
            match(opcao):
                # cadastrar usuário
                case 1:
                    print("Preencha as informações requeridas, acerca do usuário.")
                    
                    is_adm = str(input("Administrador? [S/N]: ")).upper()
                    usuario.formatarADM(is_adm)

                    nome = str(input("Nome: "))
                    usuario.formatarNome(nome)

                    cpf = str(input("CPF: "))
                    usuario.formatarCPF(cpf)
                        
                    senha = str(input("Senha: "))
                    usuario.formatarSenha(senha)
                        
                    email = str(input("Email: "))
                    usuario.formatarEmail(email)

                    telefone = str(input("Telefone: "))
                    usuario.formatarTelefone(telefone)

                    apartamento = str(input("Apartamento: "))
                    usuario.formatarApartamento(apartamento)
                    
                    usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), is_adm, nome, cpf, senha, email, telefone, apartamento)
                    
                    if usuario_cadastrado:
                        print(f"Usuário {nome.upper()} cadastrado com sucesso!")
                    
                    time.sleep(2)
                    choiceAdm()
                        
                    # solicitar as informações para o usuario
                    # criar uma função para tratar os dados (models)
                    # chamar a função
                    # tratar os dados dentro da função
                    # verificar se a ação deu certo
                    
                # listar usuário
                case 2:
                    with open('database/usuarios.json', 'r') as arquivo:
                        read = arquivo.read()
                        data = json.loads(read)
                        print(data)
                    while True:
                        usuario_encontrado = False
                        print('Digite B para buscar um usuário em específico.')
                        print('Se deseja voltar ao menu de gerenciamento de usuários, digite M.')
                        pOpc = str(input('Digite aqui: ')).upper()
                        print("-"*20)
                        
                        if pOpc == 'B':
                            nome = str(input('Usuário a ser buscado: ')).upper()

                            buscarUsuario = usuario.buscarUsuario()
                            for c in buscarUsuario:
                                if nome in c['nome'].upper():
                                    print(f"{c['id']} - {c['nome']}")
                                    usuarioEncontrado = True
                            
                            if not usuarioEncontrado:
                                msg_alerta = f"Alerta: Usuário {buscarUsuario} não existe. Tente novamente ou cadastre esse usuário." 
                                print(msg_alerta)

                            sOpc = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            while sOpc not in ("SN"):
                                print("Opção inválida! Tente novamente.")
                                opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                            if opcao == "N":
                                print('Voltando ao menu...')
                                time.sleep(1)
                                choiceAdm()
                                break
                        
                        elif pOpc == "M":
                            choiceAdm()

                        while pOpc != 'B' and pOpc != 'M':
                            print('Opcão inválida! Por favor, tente novamente.')
                            print('Digite B para buscar um usuário específico.')
                            print('Se deseja voltar ao menu de gerenciamento de usuários, digite M.')
                            pOpc = str(input('Digite aqui: ')).upper()

                # atualizar usuário    
                case 3:
                    with open('database/usuarios.json', 'r') as arquivo:
                        read = arquivo.read()
                        data = json.loads(read)
                        print(data)

                    while True:
                        print("-"*20)
                        user_to_update = str(input("Usuario para atualizar: ")).upper()
                        print("-"*20)
                        
                        # verifica se usuario existe
                        user_updated = usuario.atualizarUsuario(user_to_update)
                        
                        if user_updated:
                            os.system('cls')
                            print(f"Usuário {user_to_update} atualizado com sucesso!") 
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not user_updated:
                            os.system('cls')
                            print(f"Alerta: Usuário {user_to_update} não existe. Tente novamente ou cadastre esse usuário.")
                            time.sleep(2) 
                    
                # deletar usuário
                case 4: 
                    while True:
                        print("-"*20)
                        user_to_delete = str(input("Usuario para deletar: ")).upper()
                        print("-"*20)
                        
                        # verifica se usuario existe
                        user_deleted = usuario.deletarUsuario(user_to_delete)
                        
                        if user_deleted:
                            os.system('cls')
                            print(f"Usuário {user_to_delete} deletado com sucesso!") 
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not user_deleted:
                            os.system('cls')
                            print(f"Alerta: Usuário {user_to_delete} não existe ou já foi deletado. Tente novamente ou cadastre esse usuário.")
                            time.sleep(2) 
                        
                        choiceAdm()
                
                # voltar
                case 0:
                    time.sleep(1)
                    choiceAdm()
                    
                # opção incorreta 
                case 10:
                    print("Saindo...")
                    time.sleep(2)
                    exit()

                case __:
                    print('Opção inválida! Por favor, tente novamente.')
                    choiceAdm()
        
        # GERENCIAR CONDOMÍNIOS
        case "2": 
            menuGerenciarCondominio()
            opcao = int(input("Digite uma opção: "))
            
            # cadastrar condomínio
            if opcao == 1:
                nome_cond = str(input("Nome do condomínio: "))
                rua = str(input("Rua: "))
                bairro = str(input("Bairro: "))
                cidade = str(input("Cidade: "))
                estado = str(input("Estado: [UF] ")).upper()
                
                endereco = rua + ", " + bairro + " - " + cidade + "/" + estado 
               
                cep = str(input("CEP: "))
                condominio.formatarCEP(cep)
                    
                qntd_andares = str(input("Quantidade de andares: "))      
                qntd_apto = str(input("Quantidade de apartamentos: "))
                
                condominio_cadastrado = condominio.cadastrarCondominio(condominio.obter_proximo_id(), nome_cond, endereco, cep, qntd_andares, qntd_apto)
                
                if condominio_cadastrado:
                    print(f"Condomínio {nome_cond.upper()} / CEP: {cep} cadastrado com sucesso!")
                
                time.sleep(2)
                choiceAdm()
                    
                # solicitar as informações para o usuario
                # criar uma função para tratar os dados (models)
                # chamar a função
                # tratar os dados dentro da função
                # verificar se a ação deu certo
                
            # listar condomínios
            elif opcao == 2:
                while True:
                    condominio_encontrado = False
                    
                    buscar_condominio = condominio.buscarCondominio()
                    for c in buscar_condominio:
                        print(f"{c['id']} - {c['nome']}")
                        
                    nome = str(input("Condomínio para buscar: ")).upper()
                    print("-"*20)
                    
                    for c in buscar_condominio:
                        if nome in c['nome'].upper():
                            print(f"Nome: {c['nome']} \nEndereço: {c['endereco']}")
                            condominio_encontrado = True
                    
                    if not condominio_encontrado:
                        msg_alerta = f"Alerta: Condomínio {buscar_condominio} não existe. Tente novamente ou cadastre esse condomínio." 
                        print(msg_alerta)

                    opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                    while opcao not in ("SN"):
                        print("Opção inválida! Tente novamente.")
                        opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                    
                    if opcao in "N":    
                        time.sleep(1)
                        choiceAdm()
                        break
            
            # atualizar condomínios    
            elif opcao == 3:
                while True:
                    print("-"*20)
                    cond_to_update = str(input("Condomínio para atualizar: ")).upper()
                    print("-"*20)
                    
                    # verifica se usuario existe
                    cond_updated = condominio.atualizarCondominio(cond_to_update)
                    
                    if cond_updated:
                        os.system('cls')
                        print(f"Condomínio {cond_to_update} atualizado com sucesso!") 
                        time.sleep(2)
                        choiceAdm()
                        break

                    elif not cond_updated:
                        os.system('cls')
                        print(f"Alerta: Condomínio {cond_to_update} não existe. Tente novamente ou cadastre esse condomínio.")
                        time.sleep(2) 
                
            # deletar condomínios
            elif opcao == 4: 
                while True:
                    print("-"*20)
                    cond_to_delete = str(input("Condomínio para deletar: ")).upper()
                    print("-"*20)
                    
                    # verifica se usuario existe
                    cond_deleted = condominio.deletarCondominio(cond_to_delete)
                    
                    if cond_deleted:
                        os.system('cls')
                        print(f"Condomínio {cond_to_delete} deletado com sucesso!") 
                        time.sleep(2)
                        choiceAdm()
                        break

                    elif not cond_deleted:
                        os.system('cls')
                        print(f"Alerta: Condomínio {cond_to_delete} não existe ou já foi deletado. Tente novamente ou cadastre esse condomínio.")
                        time.sleep(2) 
                    
                    choiceAdm()
            
            # sair
            elif opcao == 5:
                time.sleep(1)
                choiceAdm()
                
            # opção incorreta 
            else:
                print("Opção inválida!")
                time.sleep(2)
                choiceAdm()
                
                
        # GERENCIAR RESERVA
        case "3": 
            
            print(opc)
            
        # Comunicação
        case "4": 
            
            print(opc)
        
        # SAIR
        case "5":  
            main.main()
            
        # OPCÃO INVÁLIDA
        case __:
            print("Opção inválida!")
            time.sleep(2)
            choiceAdm()
    
    