import os

def menu():
    print('-='*7)
    print('IDENTIFICAÇÃO')
    print('-='*7)

    print('1 - Fazer login')
    print('2 - Novo na ferramenta (obter ID)')
    print('3 - Sou DEV')

def choice():
    opcao = int(input('Insira o número aqui -> '))

    match (opcao):
        case 1:
            print('-='*4)
            print('LOGIN - MORADOR/GESTOR')
            print('-='*4)

            id = str(input('Insira seu ID -> ')
            #PUXAR FUNÇÃO DA PAGINA INICIAL MORADOR/GESTOR
        
        case 2:
            print('-='*15)
            print('CADASTRAR NA PLATAFORMA E OBTER ID')
            print('-='*15)

            print('Selecione o que você deseja cadatrar)
            print('1 - Quero cadastrar meu condomínio (gestor)')
            print('2 - Quero me cadastrar (morador)')
            print('3 - Voltar ao menu')

            opcaoCadastro = int(input('Digite a opção escolhida -> )

            match (opcaoCadastro):
                case 1:
                    print('-='*25)
                    print('CADASTRAR CONDOMÍNIO E GESTOR')
                    print('-='*25)
                    
                                 
            classe = str(input('Informe

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
