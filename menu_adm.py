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
 
def choiceAdm():
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
                    choiceAdm()
                        
                # LISTA DE USUÁRIOS
                case 2:
                    file = 'database/usuarios.json'
                    with open(file, mode='r') as arquivo:
                        read = arquivo.read()
                        data = json.loads(read)
                        print(data)
                    while True:
                        usuarioEncontrado = False
                        print('Digite B para buscar um usuário específico.')
                        print('Se deseja voltar ao menu de gerenciamento de usuários, digite M.')
                        pOpc = str(input('Digite aqui: ')).upper()
                        if pOpc == 'B':
                            nome = str(input("Usuário a ser buscado: ")).upper()
                            print("-"*20)
                            
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
                                sOpc = str(input("Deseja realizar outra pesquisa? [S/N] ")).upper()
                            
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
                            

                
                # ATUALIZAR USUÁRIO    
                case 3:
                    file = 'database/usuarios.json'
                    with open(file, mode='r') as arquivo:
                        read = arquivo.read()
                        data = json.loads(read)
                        print(data)
                    
                    while True:
                        usuario.atualizarUsuario()
                        '''usuarioAtualizado = False
                        userAtt = str(input('Informe o usuário que deseja atualizar: ')).upper()
                        buscarUsuario = usuario.buscarUsuario()
                        
                        for c in buscarUsuario:
                            print(f'{c['id']} - {c['nome']}')
                            usuarioAtualizado = True
                            
                            is_adm = str(input("Administrador? [S/N]: ")).upper()
                            usuario.formatarADM(is_adm)
                            
                            nome = str(input("Novo nome: "))
                            usuario.formatarNome(nome)

                            cpf = str(input('Novo CPF: '))
                            usuario.formatarCPF(cpf)
                            
                            senha = str(input("Nova senha: "))
                            usuario.formatarSenha(senha)
                                
                            email = str(input("Novo email: "))
                            usuario.formatarEmail(email)

                            telefone = str(input("Novo telefone: "))
                            usuario.formatarTelefone(telefone)

                            apartamento = str(input("Novo apartamento: "))
                            usuario.formatarApartamento(apartamento)
                            
                            user_updated = usuario.atualizarUsuario(userAtt, nome, senha, is_adm, email, telefone, apartamento)'''
                            
                        if user_updated:
                            msg_alerta = f"Usuário {userAtt} atualizado com sucesso!" 
                            time.sleep(2)
                            choiceAdm()
                            break
                        elif not user_updated:
                            msg_alerta = f"Alerta: Usuário {userAtt} não existe. Tente novamente ou cadastre esse usuário." 
                            print(msg_alerta)

                        while not usuarioEncontrado:
                            print(f"Alerta: Usuário {nome} não existe. Tente novamente ou cadastre esse usuário.")
                            nome = str(input('Informe o usuário que deseja atualizar: ')).upper()
                    
                
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
    
def mainMenuAdm():
    menuAdm()
    choiceAdm()

if __name__ == '__main__':
    mainMenuAdm()