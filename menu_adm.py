import os, time, main
import json
import models.usuarios_model as usuario
import models.reservas_model as reservas
import models.condominio_model as condominio
import models.comunicados_model as comunicados

def menuAdm():
    os.system('cls')
    print("="*23)
    print(" MENU DE ADMINISTRADOR ")
    print("="*23)
    
    print("1. Gerenciar usuários") # CRUD USUÁRIOS
    print("2. Gerenciar condomínios") # CRUD Condomínios
    print("3. Gerenciar reservas") # CRUD Reservas
    print("4. Avisos e Notificações") # CRUD Comunicação
    print("5. Chamados") # CRUD Comunicação
    print("6. Chat") # CRUD Comunicação
    print("0. Sair")
    
def menuGerenciarUsuario():
    os.system('cls')
    print("="*20)
    print(" GERENCIAR USUÁRIOS ")
    print("="*20)
    
    print("1. Cadastrar um usuário") 
    print("2. Listar usuários") 
    print("3. Atualizar um usuário")  
    print("4. Deletar um usuário") 
    print("0. Voltar")
    
def menuGerenciarCondominio():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR CONDOMÍNIO ")
    print("="*21)

    print("1. Cadastrar condomínio") 
    print("2. Listar condomínio") 
    print("3. Atualizar condomínio")  
    print("4. Deletar condomínio") 
    print("0. Voltar")
    
def menuAvisosNotificacoes():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR CONDOMÍNIO ")
    print("="*21)

    print("1. Cadastrar condomínio") 
    print("2. Listar condomínio") 
    print("3. Atualizar condomínio")  
    print("4. Deletar condomínio") 
    print("0. Voltar")
 
def menuChamados():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR CONDOMÍNIO ")
    print("="*21)

    print("1. Cadastrar condomínio") 
    print("2. Listar condomínio") 
    print("3. Atualizar condomínio")  
    print("4. Deletar condomínio") 
    print("0. Voltar")

def menuChat():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR CONDOMÍNIO ")
    print("="*21)

    print("1. Cadastrar condomínio") 
    print("2. Listar condomínio") 
    print("3. Atualizar condomínio")  
    print("4. Deletar condomínio") 
    print("0. Voltar")
      
def choiceAdm():
    menuAdm()
    opc = str(input("Digite a opção: "))
    match(opc):
        
        # GERENCIAR USUÁRIOS
        case "1":  
            menuGerenciarUsuario()
            opcao = str(input("Digite uma opção: "))
            
            match(opcao):
                # cadastrar usuário
                case "1":
                    os.system('cls')
                    print("Preencha as informações requeridas, acerca do usuário:")
                    print("-"*54)
                    
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
                        os.system('cls')
                        msg = f"Usuário {nome.upper()} cadastrado com sucesso!"
                        
                        print("="*len(msg))
                        print(msg)
                        print("="*len(msg))
                    
                    time.sleep(2)
                    choiceAdm()
                                 
                # listar usuário
                case "2":
                    os.system('cls')
                    usuarios = usuario.buscarUsuario()
                    for u in usuarios:
                        print(f"{u['id']} - {u['nome']}")
        
                    while True:
                        usuario_encontrado = False
                        print("-"*18)
                        nome = str(input('Enter -> Voltar ao menu\nUsuário a ser buscado: ')).upper()
                        print("-"*18)
                        

                        buscarUsuario = usuario.buscarUsuario()
                        if nome == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                         
                        for c in buscarUsuario:
                            if nome in c['nome'].upper():
                                os.system('cls')
                                
                                print("Dados do usuário:")
                                print("-----------------")
                                print(f"Nome: {c['nome']} ")
                                print(f"Email: {c['email']} ")
                                print(f"ADM: {c['is_adm']} ")
                                print(f"Telefone: {c['telefone']} ")
                                print(f"Apartamento: {c['apartamento']} ")
                                usuario_encontrado = True
                        
                        if not usuario_encontrado:
                            msg_alerta = f"Alerta: Usuário {nome} não existe. Tente novamente ou cadastre esse usuário." 
                            print(msg_alerta)

                        opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        # NÃO TA PASSANDO NA VALIDAÇÃO
                        while opcao not in "SN":
                            print("Opção inválida! Tente novamente.")
                                
                            opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        if opcao == "N":
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                            
                # atualizar usuário    
                case "3":
                    os.system('cls')
                    usuarios = usuario.buscarUsuario()
                    for u in usuarios:
                        print(f"{u['id']} - {u['nome']}")
                        
                    while True:
                        print("-"*20)
                        user_to_update = str(input("Enter -> Voltar ao menu\nUsuário para atualizar: ")).upper()
                        print("-"*20)
                        
                        if user_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
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
                case "4": 
                    os.system('cls')
                    usuarios = usuario.buscarUsuario()
                    for u in usuarios:
                        print(f"{u['id']} - {u['nome']}")
                        
                    while True:
                        print("-"*20)
                        user_to_delete = str(input("Enter -> Voltar ao menu\nUsuário para deletar: ")).upper()
                        print("-"*20)
                        
                        if user_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
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
                
                # voltar
                case "0":
                    time.sleep(1)
                    choiceAdm()
                
                # opcão incorreta
                case __:
                    print('Opção inválida! Por favor, tente novamente.')
                    choiceAdm()
        
        # GERENCIAR CONDOMÍNIOS
        case "2": 
            menuGerenciarCondominio()
            opcao = str(input("Digite uma opção: "))
            
            match(opcao):
                # cadastrar condomínio
                case "1":
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
                        
                # listar condomínios
                case "2":
                    os.system('cls')
                    condominios = condominio.buscarCondominio()
                    for c in condominios:
                        print(f"{c['id']} - {c['nome']}")
        
                    while True:
                        condominio_encontrado = False
                        print("-"*18)
                        nome = str(input('Enter -> Voltar ao menu\nCondominio para buscar: ')).upper()
                        print("-"*18)
                        

                        buscarCondominio = condominio.buscarCondominio()
                        if nome == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                         
                        for c in buscarCondominio:
                            if nome in c['nome'].upper():
                                os.system('cls')
                                
                                print("Dados do usuário:")
                                print("-----------------")
                                print(f"Nome: {c['nome']} ")
                                print(f"Endereço: {c['endereco']} ")
                                print(f"CEP: {c['cep']} ")
                                print(f"Andares: {c['qntd_andares']} ")
                                print(f"Apartamentos: {c['qntd_apto']} ")
                                condominio_encontrado = True
                        
                        if not condominio_encontrado:
                            msg_alerta = f"Alerta: Condomínio {nome} não existe. Tente novamente ou cadastre esse condomínio." 
                            print(msg_alerta)

                        opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        # NÃO TA PASSANDO NA VALIDAÇÃO
                        while opcao not in "SN":
                            print("Opção inválida! Tente novamente.")
                                
                            opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        if opcao == "N":
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                
                # atualizar condomínio    
                case "3":
                    os.system('cls')
                    condominios = condominio.buscarCondominio()
                    for c in condominios:
                        print(f"{c['id']} - {c['nome']}")
                        
                    while True:
                        print("-"*20)
                        cond_to_update = str(input("Enter -> Voltar ao menu\Condomínio para atualizar: ")).upper()
                        print("-"*20)
                        
                        if cond_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
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
                    
                # deletar condomínio
                case "4": 
                    os.system('cls')
                    condominios = condominio.buscarCondominio()
                    for c in condominios:
                        print(f"{c['id']} - {c['nome']}")
                        
                    while True:
                        print("-"*20)
                        cond_to_delete = str(input("Enter -> Voltar ao menu\nCondomínio para deletar: ")).upper()
                        print("-"*20)
                        
                        if cond_to_delete == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        # verifica se condomínio existe
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
                
                # voltar
                case "0":
                    time.sleep(1)
                    choiceAdm()
                    
                # opção incorreta 
                case __:
                    print("Opção inválida!")
                    time.sleep(2)
                    choiceAdm()
                        
        # GERENCIAR RESERVAS
        case "3":     
            print(opc)
            
        # AVISOS E NOTIFICAÇÕES
        case "4":  
            print(opc)
            
        # CHAMADOS
        case "5":  
            print(opc)
            
        # CHAT
        case "6":  
            print(opc)
        
        # SAIR
        case "0":  
            main.main()
            
        # OPCÃO INVÁLIDA
        case __:
            print("Opção inválida!")
            time.sleep(2)
            choiceAdm()
    
    