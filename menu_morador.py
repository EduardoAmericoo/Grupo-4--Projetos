import os, time, main
import models.usuarios_model as usuario

def menu_morador():
    os.system('cls')
    print("="*21)
    print(" MENU DE MORADOR ")
    print("="*21)
    
    print("1. Usuário")
    print("2. Reserva de áreas comuns")
    print("3. Avisos e Notificações")
    print("4. Chamados")
    print("5. Chat")
    print("0. Sair")

def menu_usuario():
    print('='*20)
    print('Menu Usuário')
    print('='*20)

    print('1. Listar informações')
    print('2. Editar informações')

def opcoes_morador():
    menu_morador()
    print("Insira a opção escolhida: ")
    menu_morador()
    opc = str(input("Insira a opção escolhida: "))
    match(opc):
        #MENU DO USUÁRIO
        case '1':
            menu_usuario()
            escolha = str(input('Digite uma opção '))
            match(escolha):
                #LISTAR INFORMAÇÕES
                case '1':
                    os.system('cls')
                    while True:
                        usuario_encontrado = False
                        print("-"*18)
                        
                        nome = str(input('Enter -> Voltar ao menu\nInsira o seu nome: ')).upper()
                        print("-"*18)
                        

                        buscarUsuario = usuario.buscarUsuario()
                        if nome == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            opcoes_morador()
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
                             msg_alerta = f"Alerta: Usuário {nome} não existe. Você inseriu o seu nome errado, tente novamente!" 
                             print(msg_alerta)
                        
                        opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        while opcao not in "SN":
                            print("Opção inválida! Tente novamente.")
                                
                            opcao = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
                        if opcao == "N":
                            print('Voltando ao menu...')
                            time.sleep(1)
                            opcoes_morador()
                            break
                
                #Editar Informações
                case '2':
                    os.system('cls')
                    while True:
                        print("-"*20)
                        user_to_update = str(input("Enter -> Voltar ao menu\nInforme o seu nome: ")).upper()
                        print("-"*20)
                        
                        if user_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            opcoes_morador()
                            break
                        
                        user_updated = usuario.atualizarUsuario(user_to_update)
                        
                        if user_updated:
                            os.system('cls')
                            print(f"Usuário {user_to_update} atualizado com sucesso!") 
                            time.sleep(2)
                            opcoes_morador()
                            break

                        elif not user_updated:
                            os.system('cls')
                            print(f"Alerta: Usuário {user_to_update} não existe. Tente novamente ou Contate o seu gestor.")
                            time.sleep(2) 
       
        # RESERVA DE ÁREAS COMUNS
        case '2':
            print('Reserva de Áreas comuns')
        # AVISOS E COMUNICAÇÕES
        case '3':
            print('Avisos e Notificações')
        # CHAMADOS
        case '4':
            print('chamados')
        #CHAT
        case '5':
            print('Chat')
        #SAIR
        case '0':
            main.main()

        #OPÇÃO INVÁLIDA
        case __:
            print('Opção inválida!')
            time.sleep(2)
            menu_morador()

def main(cpf):
    global nome_login, id_login, is_adm_login, cpf_login, senha_login, email_login, telefone_login, apartamento_login
    usuario_logado = usuario.dadosUsuarioAutenticado(cpf)
    
    id_login = usuario_logado['id']
    is_adm_login = usuario_logado['is_adm']
    nome_login = usuario_logado['nome']
    cpf_login = usuario_logado['cpf']
    senha_login = usuario_logado['senha']
    email_login = usuario_logado['email']
    telefone_login = usuario_logado['telefone']
    apartamento_login = usuario_logado['apartamento']
    
    opcoes_morador()