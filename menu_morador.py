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
                        buscarUsuario = usuario.buscarUsuario()

                        for c in buscarUsuario:
                            if cpf_login in c['cpf'].upper():
                                os.system('cls')
                                
                                print("Dados do usuário:")
                                print("-----------------")
                                print(f"Nome: {c['nome']} ")
                                print(f"Email: {c['email']} ")
                                print(f"ADM: {c['is_adm']} ")
                                print(f"Telefone: {c['telefone']} ")
                                print(f"Apartamento: {c['apartamento']} ")
                
                        opcao = str(input("Digite enter para sair: ")).upper()

                        while opcao not in "":
                            print("Opção inválida! Tente novamente.")
                                
                            opcao = str(input("Digite enter para sair: ")).upper()
                            
                        if opcao == "":
                            print('Voltando ao menu...')
                            time.sleep(1)
                            opcoes_morador()
                            break
                
                #Editar Informações
                case '2':
                    os.system('cls')
                    while True:
            
                        user_updated = usuario.atualizarUsuario(cpf_login)
                        
                        if user_updated:
                            os.system('cls')
                            print(f"Usuário propietário do cpf; {cpf_login} atualizado com sucesso!") 
                            time.sleep(2)
                            opcoes_morador()
                            break

                        elif not user_updated:
                            os.system('cls')
                            print(f"Alerta: Usuário proprietário do cpf:{cpf_login}, não existe. Tente novamente ou Contate o seu gestor.")
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
            print("Saindo...")
            time.sleep(2) 

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