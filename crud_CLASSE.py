import os

def menu():
    print('-='*7)
    print('IDENTIFICAÇÃO')
    print('-='*7)

    print('1 - Sou morador')
    print('2 - Sou síndico/gestor')
    print('3 - Sou DEV')

def choice():
    opcao = int(input('Insira o número aqui -> '))

    match (opcao):
        case 1:
            print('-='*4)
            print('MORADOR')
            print('-='*4)
        
        case 2:
            print('-='*15)
            print('SÍNDICO, GESTOR, ETC')
            print('-='*15)

        case 3:
            print('-='*2)
            print('DEV')
            print('-='*2)

        case __:
            print('Opção inváida! Por favor, tente novamente.')
            main()

def main():
    os.system('cls')
    menu()
    choice()

if __name__ == '__main__':
    main()