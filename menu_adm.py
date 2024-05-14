import os
import models.usuarios_model as usuario
import time 

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
    
    print("1. Cadastrar usuário") # CRUD USUÁRIOS
    print("2. Listar usuário") # CRUD Condomínios
    print("3. Atualizar usuário") # CRUD Áreas comuns 
    print("4. Deletar usuário") # CRUD Reservas
    print("5. Sair")

def gerenciarCondominio():
    os.system('cls')
    print("="*21)
    print(" Gerenciar Condomínio ")
    print("="*21)
    
    print("1. Cadastrar condomínio") # CRUD USUÁRIOS
    print("2. Listar condomínio") # CRUD Condomínios
    print("3. Atualizar condomínio") # CRUD Áreas comuns 
    print("4. Deletar condomínio") # CRUD Reservas
    print("5. Sair")
    
def gerenciarReservas():
    os.system('cls')
    print("="*21)
    print(" Gerenciar Usuários ")
    print("="*21)
    
    print("1. Cadastrar usuário") # CRUD USUÁRIOS
    print("2. Listar usuário") # CRUD Condomínios
    print("3. Atualizar usuário") # CRUD Áreas comuns 
    print("4. Deletar usuário") # CRUD Reservas
    print("5. Sair")
    
def comunicacao():
    os.system('cls')
    print("="*21)
    print(" Gerenciar Usuários ")
    print("="*21)
    
    print("1. Cadastrar usuário") # CRUD USUÁRIOS
    print("2. Listar usuário") # CRUD Condomínios
    print("3. Atualizar usuário") # CRUD Áreas comuns 
    print("4. Deletar usuário") # CRUD Reservas
    print("5. Sair")

def opcoes_adm():
    menu_adm()
    opc = str(input("Digite a opção: "))
    match(opc):
        
        
        case "1": # Gerenciar Usuários 
            gerenciarUsuario()
            opcao = int(input("Digite uma opção: "))
            
                
            match(opcao):
                case 1:
                    # cadastrar usuario
                    nome = str(input("Digite seu nome: "))
                    cpf = str(input("Digite seu cpf: "))
                    senha = str(input("Digite seu senha: "))
                    email = str(input("Digite seu email: "))
                    tipo_user = str(input("Tipo de usuario: [0 - Morador / 1 - Adm] "))
                    telefone = str(input("Digite seu telefone: "))
                    apartamento = str(input("Digite seu apartamento: "))
                    
                    usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), tipo_user, nome, cpf, senha, email, telefone, apartamento)
                    
                    if usuario_cadastrado:
                        print(f"Usuário {nome.upper()} cadastrado com sucesso!")
                    
                    opcoes_adm()
                
                case __:
                    # listar usuario
                    print("Opção inválida!")
                    time.sleep(2)
                    opcoes_adm()
                
        case "2": # Gerenciar condomínios 
            
            print(opc)
        case "3": # Gerenciar reservas 
            
            print(opc)
        case "4": # Comunicação 
            
            print(opc)
        case "5":  
            print("Saindo...")
        case __:
            print(opc, "Errou")
    
    