# Implementar módulos e tratamento de erros.
import os
import time
import models.usuarios_model as usuario
import menu_adm
import menu_morador

def formatMensagemError(msg):
    tam = len(msg) + 2 
    
    print("\033[1;31m=\033[m"*tam)
    print(f"\033[1;31m {msg} \033[m")
    print("\033[1;31m=\033[m"*tam)

def formatMensagemValid(msg):
    tam = len(msg) + 2 
    
    print("\033[1;32m=\033[m"*tam)
    print(f"\033[1;32m {msg} \033[m")
    print("\033[1;32m=\033[m"*tam)
    
def menuPrincipal():
    os.system('cls')
    print("="*25)
    print(" BEM VINDO(A) À CONDTECH ")
    print("="*25)
    
    print("1. Fazer login") 
    print("2. Se cadastrar como gestor")
    print("0. Sair do sistema") 

def choiceLogin():  
    menuPrincipal()
    opc = str(input("Digite uma opção: "))
    
    match(opc):
        case "1":
            while True:
                os.system('cls')
                print("="*7)
                print(" LOGIN ")
                print("="*7)

                cpf = str(input("CPF: "))
                senha = str(input("Senha: "))
                print("="*21)
                
                # autentica o usuário 
                usuario_autenticado = usuario.autenticar_usuario(cpf, senha)
                
                if usuario_autenticado == False:
                    os.system('cls')
                    msg = "Erro na autenticação do usuário!"
                    formatMensagemError(msg)
                    time.sleep(2)
                else:
                    break
            
            # Verifica se o usuário é um morador ou adm
            if usuario_autenticado:
                os.system('cls')
                msg = "Usuário autenticado com sucesso!"
                formatMensagemValid(msg)
                time.sleep(2)


                is_adm = usuario.is_adm
            
                if is_adm is False:
                    # Menu morador
                    menu_morador.main(cpf)   
                
                elif is_adm is True:    
                    # Menu ADM
                    menu_adm.main(cpf)

        
        case "2":
            os.system('cls')
            print("="*22)
            print(" CADASTRO DE GESTORES ")
            print("="*22)
            
            nome = str(input("Digite seu nome: "))
            usuario.formatarNome(nome)
            
            cpf = str(input("Digite seu cpf: "))
            usuario.formatarCPF(cpf)
                
            senha = str(input("Digite seu senha: "))
            usuario.formatarSenha(senha)
    
            email = str(input("Digite seu email: "))      
            usuario.formatarEmail(email)
            
            telefone = str(input("Digite seu telefone: "))
            usuario.formatarTelefone(telefone)
            
            apartamento = str(input("Digite seu apartamento: "))
            usuario.formatarApartamento(apartamento)
            
            is_adm = True
            
            usuario_cadastrado = usuario.cadastrarUsuario(usuario.obter_proximo_id(), is_adm, nome, cpf, senha, email, telefone, apartamento)
            
            if usuario_cadastrado:
                print(f"Usuário {nome.upper()} cadastrado com sucesso!")
            
            time.sleep(2)
            main()
        
        case "0":
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