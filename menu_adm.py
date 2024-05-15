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

def opcoes_adm():
    menu_adm()
    opc = str(input("Digite a opção: "))
    match(opc):
        
        # Gerenciar Usuários 
        case "1":  
            gerenciarUsuario()
            opcao = int(input("Digite uma opção: "))
            
            # cadastrar usuário
            if opcao == 1:
                    nome = str(input("Digite seu nome: "))
                    cpf = str(input("Digite seu cpf: "))
                    senha = str(input("Digite seu senha: "))
                    email = str(input("Digite seu email: "))
                    tipo_user = str(input("Tipo de usuario: [0 - Morador / 1 - Adm] "))
                    while tipo_user not in "01":
                        print("Opção inválida!")
                        tipo_user = str(input("Tipo de usuario: [0 - Morador / 1 - Adm] "))
                    telefone = str(input("Digite seu telefone: "))
                    apartamento = str(input("Digite seu apartamento: "))
                    
                    usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), tipo_user, nome, cpf, senha, email, telefone, apartamento)
                    
                    if usuario_cadastrado:
                        print(f"Usuário {nome.upper()} cadastrado com sucesso!")
                    
                    time.sleep(2)
                    opcoes_adm()
                    
            # listar usuário
            elif opcao == 2:
                nome = str(input("Digite o usuário: "))
                result = usuario.listarUsuario(nome)

                print(result)
                    
                # opcoes_adm()
            
            # atualizar usuário    
            elif opcao == 3:
                
                opcoes_adm()
            
            # deletar usuário
            elif opcao == 4: 
                
                opcoes_adm()
            
            # sair
            elif opcao == 5:
                
                opcoes_adm()
                
            # opção incorreta 
            else:
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
            print("Opção inválida!")
            time.sleep(2)
            opcoes_adm()
    
    