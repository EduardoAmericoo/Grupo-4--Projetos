# Implementar módulos e tratamento de erros.
import os
import time
import models.usuarios_model as usuario
import menu_adm
import menu_morador

def menuPrincipal():
    os.system('cls')
    print("="*21)
    print(" BEM VINDO(A) AO SISTEMA ")
    print("="*21)
    
    print("1. Fazer login") 
    print("2. Se cadastrar como gestor")
    print("0. Sair do sistema") 

def choiceLogin():  
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    
    match(opc):
        case 1:
            os.system('cls')
            print("="*21)
            print(" LOGIN ")
            print("="*21)

            while True:
                print("="*21)
                cpf = str(input("CPF: "))
                senha = str(input("Senha: "))
                print("="*21)
                
                # autentica o usuário 
                usuario_autenticado = usuario.autenticar_usuario(cpf, senha)
                
                if usuario_autenticado == False:
                    print("Usuário inválido, tente novamente!")
                else:
                    break
            
            # Verifica se o usuário é um morador ou adm
            if usuario_autenticado:
                is_adm = usuario.is_adm
            
                if is_adm is False:
                    # Menu morador
                    menu_morador.opcoes_morador()     
                
                elif is_adm is True:    
                    # Menu ADM
                    menu_adm.opcoes_adm()      
                else:
                    main()
        case 2:
            os.system('cls')
            print("="*22)
            print(" CADASTRO DE GESTORES ")
            print("="*22)
            
            nome = str(input("Digite seu nome: "))
            cpf = str(input("Digite seu cpf: "))
            usuario.formatarCPF(cpf)
                
            senha = str(input("Digite seu senha: "))
            usuario.formatarSenha(senha)
    
            email = str(input("Digite seu email: "))      
            telefone = str(input("Digite seu telefone: "))
            apartamento = str(input("Digite seu apartamento: "))
            is_adm = True
                    
            usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), is_adm, nome, cpf, senha, email, telefone, apartamento)
            
            if usuario_cadastrado:
                print(f"Usuário {nome.upper()} cadastrado com sucesso!")
            
            time.sleep(2)
            main()
        
        case 0:
            print("Saindo...")
            time.sleep(2)
        
        case __:
            print("Opção inválida! Tente novamente.")
            time.sleep(2)
            main() 

def main():
    os.system('cls')
    choiceLogin()

if __name__ == '__main__':
    main()