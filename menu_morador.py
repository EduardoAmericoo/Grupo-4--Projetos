import os, time
import models.usuarios_model as usuario
import models.reservas_model as reservas
import models.chat_model as chat

def menu_morador():
    os.system('cls')
    print("="*21)
    print(" MENU DE MORADOR ")
    print("="*21)
    
    print("1. Usuário")
    print("2. Reserva de áreas comuns")
    print("3. Chat")
    print("0. Sair")

def opcoes_morador():
    menu_morador()
    opc = str(input("Digite uma opção: "))
    
    match(opc):
    
        # EXIBIR USUÁRIO E ATUALIZAR
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
                        print(f"Nome: {c['cpf']} ")
                        print(f"Email: {c['email']} ")
                        print(f"ADM: {c['is_adm']} ")
                        print(f"Telefone: {c['telefone']} ")
                        print(f"Apartamento: {c['apartamento']} ")
                
                opcao = str(input("\nDeseja atualizar o usuario? [S/N]")).upper()
                    
                while opcao not in "SN": 
                    opcao = str(input("\nOpção inválida. Deseja atualizar o usuario? [S/N]")).upper()

                    if opcao == "S":
                        break

                if opcao == "N":
                    print('Voltando ao menu...')
                    time.sleep(1)
                    opcoes_morador()
                    break

                elif opcao == "S":
                    user_updated = usuario.atualizarUsuarioMorador(cpf_login)
                    
                    if user_updated:
                        os.system('cls')
                        print(f"Usuário atualizado com sucesso!") 
                        time.sleep(2)
                        opcoes_morador()
                        break
       
        # RESERVA FAZER
        case '2':
            print('Reserva de Áreas comuns')

        # CHAT
        case '3':
            while True: 
                os.system('cls')
                print("="*16)
                print("      CHAT       ")
                print("="*16)
                
                mensagens = chat.buscarMensagem()
                
                for k in mensagens:
                    print(f"{k['nome_emissor']}: {k['mensagem']}")

                print("-"*20)
                mensagem = str(input("Enter -> Voltar ao menu\nDigite sua mensagem: "))
                
                if mensagem == "":
                    print("Voltando...")
                    time.sleep(2)
                    opcoes_morador()
                    break
                
                chat.cadastrarMensagem(chat.obter_proximo_id(), nome_login, mensagem)

        #SAIR
        case '0':
            print("Saindo...")
            time.sleep(2) 
            exit()

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