# Implementar módulos e tratamento de erros.
import os
import models.usuarios_model as usuario
import menu_adm
import menu_morador

    
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
            menu_morador.opcoes_morador()     
        
        elif id_user == "1":    
            # Menu ADM
            menu_adm.opcoes_adm()      
        else:
            main()

def main():
    os.system('cls')
    login()

if __name__ == '__main__':
    main()