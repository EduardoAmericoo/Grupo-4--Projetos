# Implementar módulos e tratamento de erros.
import os
import models.usuarios_model as usuario

def menu_morador():
    print("="*21)
    print(" Menu Morador ")
    print("="*21)
    
    print("1. Usuário")
    print("2. Reserva de áreas comuns")
    print("3. Comunicação")
    print("4. Sair")
        
def menu_adm():
    print("="*21)
    print(" Menu ADM ")
    print("="*21)
    
    print("1. Gerenciar Usuários")
    print("2. Gerenciar condomínios")
    print("3. Gerenciar áreas comuns")
    print("4. Gerenciar reservas")
    print("5. Comunicação")
    print("6. Sair")
    
    
def login():  
    # Login com CPF e Senha
    print("="*21)
    print(" LOGIN NO SISTEMA ")
    
    while True:
        print("="*21) 
        cpf = str(input("CPF: ")) 
        senha = str(input("Senha: "))
        print("="*21)
        
        usuario_autenticado = usuario.autenticar_usuario(cpf, senha)
        
        if usuario_autenticado == False:
            print("Usuário inválido, tente novamente!")
        else:
            break
     
    # Verifica se o usuário é um morador ou adm
    if usuario_autenticado:
        id_user = usuario.id_user
        
        if id_user == "0":
            # Menu morador
            menu_morador()
        
        elif id_user == "1":    
            # Menu ADM
            menu_adm()
            
            opc = str(input("Digite a opção: "))
            while opc not in ("123456"):
                print("Opção inválida, Tente novamente")
                opc = str(input("Digite a opção: "))   
            
            match(opc):
                case "1": 
                    print(opc)
                case __:
                    print(opc, "Errou")            
        else:
            main()

def main():
    os.system('cls')
    login()

if __name__ == '__main__':
    main()