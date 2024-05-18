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
    print("2. Gerenciar condomínios") # CRUD Condomínios #DEPOIS
    print("3. Gerenciar reservas") # CRUD Reservas
    print("4. Comunicação") # CRUD Comunicação
    print("0. Logout")
    print("10. Sair do sistema")
    
def gerenciarUsuario():
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
 
def opcoes_adm():
    menuAdm()
    opc = int(input("Digite a opção: "))
    match(opc):
        
        # CRUD USUÁRIOS
        case 1:  
            gerenciarUsuario()
            opcao = int(input("Digite uma opção: "))
            
            match(opcao):
                # CADASTRAR USUÁRIO
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
                        
                    email = str(input("E-mail: "))
                    usuario.formatarEmail(email)

                    telefone = str(input("Telefone: "))
                    usuario.formatarTelefone(telefone)

                    apartamento = str(input("Apartamento: "))
                    usuario.formatarApartamento(apartamento)
                    
                    usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), is_adm, nome, cpf, senha, email, telefone, apartamento)
                    
                    if usuario_cadastrado:
                        print(f"Usuário {nome.upper()} cadastrado com sucesso!")
                    
                    time.sleep(2)
                    opcoes_adm()
                        
                # LISTA DE USUÁRIOS
                case 2:
                    file = 'database/usuarios.json'
                    with open(file, mode='r') as arquivo:
                        read = arquivo.read()
                        data = json.loads(read)
                        print(data)
                    while True:
                        usuario_encontrado = False
                        buscarsn = str(input('Deseja buscar um usuário em específico?'))
                        if buscarsn == 'S':
                            nome = str(input("Usuário a ser buscado: ")).upper()
                            print("-"*20)
                            
                            buscar_usuario = usuario.buscarUsuario()
                            for c in buscar_usuario:
                                if nome in c['nome'].upper():
                                    print(f"{c['id']} - {c['nome']}")
                                    usuario_encontrado = True
                            
                            if not usuario_encontrado:
                                msg_alerta = f"Alerta: Usuário {buscar_usuario} não existe. Tente novamente ou cadastre esse usuário." 
                                print(msg_alerta)

                            opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            while opcao not in ("SN"):
                                print("Opção inválida! Tente novamente.")
                                opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                            if opcao in "N":
                                print('Voltando ao menu...')
                                time.sleep(1)
                                opcoes_adm()
                                break
                
                # ATUALIZAR USUÁRIO    
                case 3:
                    usuario_encontrado = False
                    
                    while True:
                        # Exibir usuários antes de atualizar
                        # chamar a função buscarUsuario() e atribuir a uma variável
                        # for percorrendo os valores dela e dar um print nos valores de nome
                        
                        print("-"*20)
                        user_to_update = str(input("Usuario para atualizar: ")).upper()
                        print("-"*20)
                        
                        # verifica se usuario existe
                        buscar_usuario = usuario.buscarUsuario()
                        for k, v in enumerate(buscar_usuario):
                            if user_to_update in v['nome'].upper():
                                usuario_encontrado = True
                        while not usuario_encontrado:
                            print(f"Alerta: Usuário {user_to_update} não existe. Tente novamente ou cadastre esse usuário.")
                            user_to_update = str(input("Usuario para atualizar: ")).upper()
                            
                            for k, v in enumerate(buscar_usuario):
                                if user_to_update in v['nome'].upper():
                                    usuario_encontrado = True
                            
                        nome = str(input("Novo nome: "))
                        
                        senha = str(input("Nova senha: "))
                        usuario.formatarSenha(senha)
                            
                        is_adm = str(input("Usuário é adm: [S/N] ")).upper()
                        usuario.formatarADM(is_adm)
                            
                        email = str(input("Novo email: "))      
                        telefone = str(input("Novo seu telefone: "))
                        apartamento = str(input("Novo seu apartamento: "))
                        
                        user_updated = usuario.atualizarUsuario(user_to_update, nome, senha, is_adm, email, telefone, apartamento)
                        
                        if user_updated:
                            msg_alerta = f"Usuário {user_to_update} atualizado com sucesso!" 
                            time.sleep(2)
                            opcoes_adm()
                            break
                        elif not user_updated:
                            msg_alerta = f"Alerta: Usuário {user_to_update} não existe. Tente novamente ou cadastre esse usuário." 
                            print(msg_alerta)
                    
                
                # DELETAR USUÁRIO
                case 4: 
                    
                    opcoes_adm()
                
                # VOLTAR
                case 0:
                    time.sleep(1)
                    opcoes_adm()
                    
                # SAIR DO SISTEMA
                case 10:
                    print("Saindo...")
                    time.sleep(2)
                
                # opção incorreta 
                case __:
                    print("Opção inválida!")
                    time.sleep(2)
                    opcoes_adm()
        
        # GERENCIAR CONDOMÍNIOS
        case 2: 
            
            print(opc)
            
        # GERENCIAR RESERVA
        case 3: 
            
            print(opc)
            
        # Comunicação
        case 4: 
            
            print(opc)
        
        # VOLTAR AO MENU ANTERIOR
        case 0:  
            main.main()
            
        # SAIR DO SISTEMA
        case 10:
            print("Saindo...")
            time.sleep(2)
            exit()
        
        # OPCÃO INVÁLIDA
        case __:
            print("Opção inválida!")
            time.sleep(2)
            opcoes_adm()
    
    