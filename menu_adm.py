import os, time
import main as m
import models.usuarios_model as usuario
import models.reservas_model as reservas
import models.condominio_model as condominio
import models.chat_model as chat

def menuAdm():
    os.system('cls')
    print("="*23)
    print(" MENU DE ADMINISTRADOR ")
    print("="*23)
    
    print("1. Gerenciar usuários") 
    print("2. Gerenciar condomínios") 
    print("3. Gerenciar reservas") 
    print("4. Chat") 
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
                        m.formatMensagemValid(msg)
                    
                    time.sleep(2)
                    choiceAdm()
                                 
                # listar usuário
                case "2":
                    while True:
                        os.system('cls')
                        usuarios = usuario.buscarUsuario()
                        for u in usuarios:
                            print(f"{u['id']} - {u['nome']}")
                            
                        usuario_encontrado = False
                        
                        print("-"*18)
                        id = str(input('Enter -> voltar ao menu\nUsuário a ser buscado: '))
                        print("-"*18)  

                        buscarUsuario = usuario.buscarUsuario()
                        if id == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                         
                        for c in buscarUsuario:
                            if int(id) == c['id']:
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
                            msg_alerta = f"Alerta: Usuário {id} não existe. Tente novamente ou cadastre esse usuário." 
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
                    while True:
                        os.system('cls')
                        usuarios = usuario.buscarUsuario()
                        for u in usuarios:
                            print(f"{u['id']} - {u['nome']}")
                            
                        print("-"*20)
                        user_to_update = str(input("Enter -> voltar ao menu\nUsuário para atualizar[id]: "))
                        print("-"*20)
                        
                        if user_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        user_updated = usuario.atualizarUsuario(int(user_to_update))
                        
                        if user_updated:
                            os.system('cls')
                            msg = f"Usuário {user_to_update} atualizado com sucesso!"
                            m.formatMensagemValid(msg) 
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not user_updated:
                            os.system('cls')
                            msg = f"Alerta: Usuário {user_to_update} não existe. Tente novamente ou cadastre esse usuário."
                            m.formatMensagemError(msg)
                            time.sleep(2) 
                    
                # deletar usuário
                case "4": 
                    while True:
                        os.system('cls')
                        usuarios = usuario.buscarUsuario()
                        for u in usuarios:
                            print(f"{u['id']} - {u['nome']}")    
                
                        print("-"*20)
                        user_to_delete = str(input("Enter -> voltar ao menu\nUsuário para deletar: "))
                        print("-"*20)
                        
                        if user_to_delete == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        # verifica se usuario existe
                        user_deleted = usuario.deletarUsuario(int(user_to_delete))
                        
                        if user_deleted:
                            os.system('cls')
                            msg = f"Usuário {user_to_delete} deletado com sucesso!"
                            m.formatMensagemValid(msg) 
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not user_deleted:
                            os.system('cls')
                            msg = f"Alerta: Usuário {user_to_delete} não existe ou já foi deletado. Tente novamente ou cadastre esse usuário."
                            m.formatMensagemError(msg)
                            time.sleep(2) 
                
                # voltar
                case "0":
                    time.sleep(1)
                    choiceAdm()
                
                # opcão incorreta
                case __:
                    os.system('cls')
                    msg = 'Opção inválida! Por favor, tente novamente.'
                    m.formatMensagemError(msg)
                    time.sleep(1)
                    choiceAdm()
        
        # GERENCIAR CONDOMÍNIOS
        case "2": 
            menuGerenciarCondominio()
            opcao = str(input("Digite uma opção: "))
            
            match(opcao):
                # cadastrar condomínio
                case "1":
                    os.system('cls')
                    print("Preencha as informações requeridas, acerca do condomínio:")
                    print("-"*60)

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
                        os.system('cls')
                        msg = f"Condomínio {nome_cond.upper()} / CEP: {cep} cadastrado com sucesso!"
                        m.formatMensagemValid(msg)

                    time.sleep(2)
                    choiceAdm()
                        
                # listar condomínios
                case "2":
                    while True:
                        os.system('cls')
                        condominios = condominio.buscarCondominio()
                        for c in condominios:
                            print(f"{c['id']} - {c['nome']}")
        
                        condominio_encontrado = False
                        print("-"*18)
                        nome = str(input('Enter -> Voltar ao menu\nCondominio para buscar: '))
                        print("-"*18)
                        
                        buscarCondominio = condominio.buscarCondominio()
                        if nome == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                         
                        for c in buscarCondominio:
                            if int(nome) == c['id']:
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
                    while True:
                        os.system('cls')
                        condominios = condominio.buscarCondominio()
                        for c in condominios:
                            print(f"{c['id']} - {c['nome']}")
                        
                        print("-"*20)
                        cond_to_update = str(input("Enter -> Voltar ao menu\nCondomínio para atualizar: "))
                        print("-"*20)
                        
                        if cond_to_update == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        cond_updated = condominio.atualizarCondominio(int(cond_to_update))
                        
                        if cond_updated:
                            os.system('cls')
                            msg = f"Condomínio {cond_to_update} atualizado com sucesso!"
                            m.formatMensagemValid(msg)
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not cond_updated:
                            os.system('cls')
                            msg = f"Alerta: Condomínio {cond_to_update} não existe. Tente novamente ou cadastre esse condomínio."
                            m.formatMensagemError(msg)
                            time.sleep(2) 
                    
                # deletar condomínio
                case "4": 
                    os.system('cls')
                    condominios = condominio.buscarCondominio()
                    for c in condominios:
                        print(f"{c['id']} - {c['nome']}")
                        
                    while True:
                        print("-"*20)
                        cond_to_delete = str(input("Enter -> Voltar ao menu\nCondomínio para deletar: "))
                        print("-"*20)
                        
                        if cond_to_delete == "":
                            os.system('cls')
                            print('Voltando ao menu...')
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        # verifica se condomínio existe
                        cond_deleted = condominio.deletarCondominio(int(cond_to_delete))
                        
                        if cond_deleted:
                            os.system('cls')
                            msg = f"Condomínio {cond_to_delete} deletado com sucesso!"
                            m.formatMensagemValid(msg) 
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not cond_deleted:
                            os.system('cls')
                            msg = f"Alerta: Condomínio {cond_to_delete} não existe ou já foi deletado. Tente novamente ou cadastre esse condomínio."
                            m.formatMensagemError(msg)
                            time.sleep(2) 
                
                # voltar
                case "0":
                    time.sleep(1)
                    choiceAdm()
                    
                # opção incorreta 
                case __:
                    os.system('cls')
                    msg = "Opção inválida!"
                    m.formatMensagemError(msg)
                    time.sleep(2)
                    choiceAdm()
                        
        # GERENCIAR RESERVAS
        case "3":     
            menuGerenciarReservas()
            opcao = str(input("Digite a opção: "))

            areas_comuns = ["Piscina", "Quadra", "Churrasqueira", "Salão de Festas"]
            
            match(opcao):
                case '1': # Fazer reserva
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
                            choiceAdm()
                        
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
                                choiceAdm()
                                break                         

                case '2': # Listar reservas
                    while True:
                        os.system('cls')
                        reservas.listarReservas()
                        lista = reservas.buscarReservas()

                        if lista == []:
                            os.system('cls')
                            print("\033[1;31mNão existe nenhuma reserva agendada. Faça uma reserva!\033[m")
                            time.sleep(1)
                            choiceAdm()
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
                            choiceAdm()
                            break
                
                case '3': # alternar reserva
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
                            choiceAdm()
                            break
                        id = int(id_to_update) + 1
                        reserva_updated = reservas.atualizarReserva(id)
                        
                        if reserva_updated:
                            os.system('cls')
                            msg = f"Reserva {id_to_update} atualizada com sucesso!"
                            m.formatMensagemValid(msg)
                            time.sleep(2)
                            choiceAdm()
                            break

                        elif not reserva_updated:
                            os.system('cls')
                            msg = f"Alerta: Reserva {id_to_update} não existe. Tente novamente ou faça uma reserva."
                            m.formatMensagemError(msg)
                            time.sleep(2)
                
                case '4': # Cancelar reservas
                    while True:
                        os.system('cls')
                        reservas.listarReservas()
                        lista = reservas.buscarReservas() 
                        reserva_cancelada = False
                        
                        if lista == []:
                            os.system('cls')
                            print("\033[1;31mNão existe nenhuma reserva agendada. Faça uma reserva!\033[m")
                            time.sleep(1)
                            choiceAdm()
                            break
                        
                        reserva_id = str(input("Enter -> Voltar para o menu\nInsira o ID da reserva que deseja cancelar: "))

                        if reserva_id.isdigit() and 0 <= int(reserva_id) < len(lista):
                            reserva_cancelada = reservas.cancelarReserva(reserva_id, lista)
                        elif reserva_id == "":
                            os.system('cls')
                            print("Voltando...")
                            time.sleep(1)
                            choiceAdm()
                            break
                        else:
                            print("\033[1;31mNúmero da reserva inválido.\033[m")
                            time.sleep(1)
                        
                        if reserva_cancelada:
                            os.system('cls')
                            print("\033[1;32mReserva cancelada com sucesso!\033[m")
                            time.sleep(1)
                            choiceAdm()
                            break

                case '0': # Voltando
                    time.sleep(1)
                    choiceAdm()
                
                case __: # Opcão incorreta
                    os.system('cls')
                    msg = "Opção inválida!"
                    m.formatMensagemError(msg)
                    time.sleep(2)
                    choiceAdm()
        
        # CHAT
        case "4":  
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
                    choiceAdm()
                    break
                
                chat.cadastrarMensagem(chat.obter_proximo_id(), nome_login, mensagem)
            
        # SAIR
        case "0":  
            print("Saindo...")
            time.sleep(2)
            exit()
            
        # OPCÃO INVÁLIDA
        case __:
            os.system('cls')
            msg = "Opção inválida!"
            m.formatMensagemError(msg)
            time.sleep(2)
            choiceAdm()
    
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
    
    choiceAdm()
    