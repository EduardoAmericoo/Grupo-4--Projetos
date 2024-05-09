import os

condominio = dict()
cadastros = list()

def menu():
    print('='*22)
    print('SISTEMA DE CONDOMÍNIOS')
    print('='*22)

    print('1 - Cadastrar um condomínio')
    print('2 - Exibir/buscar condomínios cadastrados')
    print('3 - Atualizar dados de um condomínio')
    print('4 - Apagar um condomínio')
    print('5 - Sair do sistema')

def choice():
    opcao = int(input('Digite a opção escolhida -> '))

    match (opcao):
        
        case 1:
            print('Cadastrar um condomínio')
            #PEDIR ENDEREÇO E FORNECER UM CÓDIGO NO FINAL

            opcao = str(input('Digite M para voltar ao menu:'))
            

        case 2:
            print('Exibir/buscar condomínios cadastrados')
            #PRIMEIRO EXIBIR TODOS OS CONDOMINIOS
            #PERGUNTAR SE DESEJA BUSCAR ALGUM ESPECIFICO
            #SE SIM, FORNECER A FERRAMENTA DE BUSCAR

            opcao = str(input('Digite M para voltar ao menu:'))

        case 3:
            print('Atualizar dados de um condomínio')
            #FERRAMENTA DE BUSCA, E LOGO DEPOIS PERGUNTAR O QUE DESEJA MUDAR

            opcao = str(input('Digite M para voltar ao menu:'))

        case 4:
            print('Apagar um condomínio')
            #FERRAMENTA DE BUSCA E MENSAGEM DE CONFIRMAÇÃO PARA APAGAR

            opcao = str(input('Digite M para voltar ao menu:'))
            

        case 5:
            print('Saindo...')
            #BIBLIOTECA DELAY

        case __:
            print('Opção inválida! Tente novamente.')
            main()

def main():
    os.system('cls')
    menu()
    choice()

if __name__ == '__main__':
    main()
