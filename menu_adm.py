import os
import time 
import main
import models.usuarios_model as usuario
import models.reservas_model as reservas
import models.condominio_model as condominio
import models.comunicados_model as comunicados

def menu_adm():
    os.system('cls')
    print("="*21)
    print(" Menu ADM ")
    print("="*21)
    
    print("1. Gerenciar usuários") # CRUD USUÁRIOS
    print("2. Gerenciar condomínios") # CRUD Condomínios
    print("3. Gerenciar reservas") # CRUD Reservas
    print("4. Comunicação") # CRUD Comunicação
    print("5. Sair") 
    
def gerenciarUsuario():
    os.system('cls')
    print("="*21)
    print(" Gerenciar Usuários ")
    print("="*21)
    
    print("1. Cadastrar usuário") 
    print("2. Listar usuário") 
    print("3. Atualizar usuário")  
    print("4. Deletar usuário") 
    print("5. Sair")
 
def opcoes_adm():
    menu_adm()
    opc = str(input("Digite a opção: "))
    match(opc):
        
        # CRUD USUÁRIOS
        case "1":  
            gerenciarUsuario()
            opcao = int(input("Digite uma opção: "))
            
            # cadastrar usuário
            if opcao == 1:
                nome = str(input("Digite seu nome: "))
                cpf = str(input("Digite seu cpf: "))
                usuario.formatarCPF(cpf)
                    
                senha = str(input("Digite seu senha: "))
                usuario.formatarSenha(senha)
                    
                is_adm = str(input("Usuário é adm: [S/N] ")).upper()
                usuario.formatarADM(is_adm)
                    
                email = str(input("Digite seu email: "))      
                telefone = str(input("Digite seu telefone: "))
                apartamento = str(input("Digite seu apartamento: "))
                
                usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), is_adm, nome, cpf, senha, email, telefone, apartamento)
                
                if usuario_cadastrado:
                    print(f"Usuário {nome.upper()} cadastrado com sucesso!")
                
                time.sleep(2)
                opcoes_adm()
                    
            # listar usuário
            elif opcao == 2:
                while True:
                    usuario_encontrado = False
                    nome = str(input("Usuario para buscar: ")).upper()
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
                        time.sleep(1)
                        opcoes_adm()
                        break
            
            # atualizar usuário    
            elif opcao == 3:
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
                
            
            # deletar usuário
            elif opcao == 4: 
                
                opcoes_adm()
            
            # sair
            elif opcao == 5:
                time.sleep(1)
                opcoes_adm()
                
            # opção incorreta 
            else:
                print("Opção inválida!")
                time.sleep(2)
                opcoes_adm()
        
        # GERENCIAR CONDOMÍNIOS
        case "2": 
            
            print(opc)
            
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
            opcoes_adm()
    
    