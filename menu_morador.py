import os, time
import main as m
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

def menuGerenciarReservas():
    os.system('cls')
    print("="*21)
    print(" GERENCIAR RESERVAS ")
    print("="*21)

    print("1. Fazer Reserva")
    print("2. Listar Reservas")
    print("3. Alterar Reserva")
    print("4. Cancelar Reserva")
    print("0. Voltar") 

def opcoes_morador():
    menu_morador()
    opc = str(input("Digite uma opção: "))
    
    match(opc):
    
        case '1':
            os.system('cls')

            while True:                        
                buscarUsuario = usuario.buscarUsuario()

                for c in buscarUsuario:
                    if id_login == c['id']:
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
                    user_updated = usuario.atualizarUsuarioMorador(id_login)
                    
                    if user_updated:
                        os.system('cls')
                        msg = "Usuário atualizado com sucesso!" 
                        m.formatMensagemValid(msg) 
                        time.sleep(2)
                        opcoes_morador()
                        break
        
        case '2':
            menuGerenciarReservas()
            opcao = str(input("Digite a opção: "))

            areas_comuns = ["Piscina", "Quadra", "Churrasqueira", "Salão de Festas"]
            
            match(opcao):
                case '1':
                    while True:
                        os.system('cls')
                        print("Áreas Comuns Disponíveis para Reserva: ")
                        print("1. Piscina")
                        print("2. Quadra")
                        print("3. Churrasqueira")
                        print("4. Salão de festas")
                        print("V. Voltar para o Menu Principal")

                        escolha = input("Escolha a área que deseja reservar (ou 'V' para voltar): ")

                        if escolha.upper() == 'V':
                            print("Voltando...")
                            time.sleep(1)
                            opcoes_morador()
                        
                        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(areas_comuns):
                            print("\033[1;31mEscolha inválida. Tente novamente.\033[m")
                            continue
                        
                        os.system('cls')
                        area_escolhida = areas_comuns[int(escolha) - 1]
                        print(f"Área escolhida: {area_escolhida}")
                        
                        while True:
                            data = input("Insira a data da reserva (dd/mm/aaaa): ")
                            if not reservas.validarData(data):
                                print("\033[1;31mData inválida ou data já passou. Tente novamente.\033[m")
                                continue

                            horario_inicio = input("Insira o horário de início da reserva (hh:mm): ")
                            if not reservas.validarHorario(horario_inicio):
                                print("\033[1;31mHorário de início inválido. Tente novamente.\033[m")
                                continue

                            horario_fim = input("Insira o horário de término da reserva (hh:mm): ")
                            if not reservas.validarHorario(horario_fim):
                                print("\033[1;31mHorário de término inválido. Tente novamente.\033[m")
                                continue
                            
                            if horario_inicio >= horario_fim:
                                print("\033[1;31mO horário de término deve ser após o horário de início. Tente novamente.\033[m")
                                continue
                        
                            reserva_salva = reservas.fazerReserva(reservas.obter_proximo_id(), nome_login, area_escolhida, data, horario_inicio, horario_fim)

                            if reserva_salva:
                                time.sleep(1)
                                opcoes_morador()
                                break                         

                case '2':
                    while True:
                        os.system('cls')
                        reservas.listarReservas()
                        lista = reservas.buscarReservas()

                        if lista == []:
                            os.system('cls')
                            print("\033[1;31mNão existe nenhuma reserva agendada. Faça uma reserva!\033[m")
                            time.sleep(1)
                            opcoes_morador()
                            break

                        opc = input("Aperte enter para voltar ao menu: ")
                        while opc not in "":
                            opc = input("Aperte enter para voltar ao menu: ")

                            if opc == "":
                                break
                            
                        if opc == "":
                            os.system('cls')
                            print("Voltando...")
                            time.sleep(1)
                            opcoes_morador()
                            break
                
                case '3':
                    while True:
                        os.system('cls')
                        reservas.listarReservas()
                        
                        print("-"*20)
                        id_to_update = str(input("Enter -> Voltar ao menu\Reserva para atualizar: [ID] "))
                        print("-"*20)
                        
                        if id_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            opcoes_morador()
                            break
                        id = int(id_to_update) + 1
                        reserva_updated = reservas.atualizarReserva(id)
                        
                        if reserva_updated:
                            os.system('cls')
                            msg = f"Reserva {id_to_update} atualizada com sucesso!"
                            m.formatMensagemValid(msg)
                            time.sleep(2)
                            opcoes_morador()
                            break

                        elif not reserva_updated:
                            os.system('cls')
                            msg = f"Alerta: Reserva {id_to_update} não existe. Tente novamente ou faça uma reserva."
                            m.formatMensagemError(msg)
                            time.sleep(2)
                
                case '4':
                    while True:
                        os.system('cls')
                        reservas.listarReservas()
                        lista = reservas.buscarReservas() 
                        reserva_cancelada = False
                        
                        if lista == []:
                            os.system('cls')
                            print("\033[1;31mNão existe nenhuma reserva agendada. Faça uma reserva!\033[m")
                            time.sleep(1)
                            opcoes_morador()
                            break
                        
                        reserva_id = str(input("Enter -> Voltar para o menu\nInsira o ID da reserva que deseja cancelar: "))

                        if reserva_id.isdigit() and 0 <= int(reserva_id) < len(lista):
                            reserva_cancelada = reservas.cancelarReserva(reserva_id, lista)
                        elif reserva_id == "":
                            os.system('cls')
                            print("Voltando...")
                            time.sleep(1)
                            opcoes_morador()
                            break
                        else:
                            print("\033[1;31mNúmero da reserva inválido.\033[m")
                            time.sleep(1)
                        
                        if reserva_cancelada:
                            os.system('cls')
                            print("\033[1;32mReserva cancelada com sucesso!\033[m")
                            time.sleep(1)
                            opcoes_morador()
                            break

                case '0':
                    time.sleep(1)
                    opcoes_morador()
                
                case __:
                    os.system('cls')
                    msg = "Opção inválida!"
                    m.formatMensagemError(msg)
                    time.sleep(2)
                    opcoes_morador()

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

        case '0':
            print("Saindo...")
            time.sleep(2) 
            exit()

        case __:
            msg = 'Opção inválida!'
            m.formatMensagemError(msg)
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
