import os

def menu():
    print('='*35)
    print('LOGIN - GERENCIAMENTO DO CONDOMÍNIO')
    print('='*35)

    print('1 - Entrar com o código do seu condomínio')
    print('2 - Solicitar cadastro de condomínio')
    print('3 - Remover seu condomínio')
    print('4 - Sair')
    
def choice():    
    opcao = int(input('Digite uma opção: '))

    match (opcao):
        case 1:
            print('Entrar com o código do seu condomínio')

        case 2:
            print('Solicitar o cadastro do seu condomínio')

        case 3:
            print('Remover seu condomínio cadastrado')

        case 4:
            print('Saindo...')

        case __:
            print('Opção inválida! Tente novamente.')

def main():
    os.system('cls')
    menu()
    choice()

if __name__ == '__main__':
    main()
  
