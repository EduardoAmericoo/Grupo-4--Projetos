import os

condominio = dict(list())
condCadastrados = list()

def menu():
    print('='*35)
    print('GERENCIAMENTO DE CONDOMÍNIO - SÍNDICO/GESTOR')
    print('='*35)

    print('1 - Gerenciar condomínio')
    print('2 - Solicitar cadastro de condomínio')
    print('3 - Remover seu condomínio')
    print('4 - Sair')
    
def choice():    
    opcao = int(input('Digite uma opção: '))

    match (opcao):

        case 1:
            print('-='*20)
            print('GERENCIAR CONDOMÍNIO(S)')
            print('-='*20)

            print('Seus condomínios:')
            for c in condCadastrados:
                print(f'{condCadastrados.index(c) + 1} - {c[condominio]}')

            def buscarCond():
                condBuscado = str(input('Qual condomínio você deseja acessar?'))
                if condBuscado in c[condominio]:
                    print(f'{condCadastrados.index(c) + 1} - {c[condominio]}')

                if condBuscado not in c[condominio]:
                    print(f'Condomínio {condBuscado} não encontrado!')
                    opcao = str(input('Deseja tentar novamente? (S/N) -> ')).upper
                    if opcao == 'S':
                        buscarCond()
                    if opcao == 'N':
                        main()
                    else:
                        print('Opção inválida! Use apenas S (para sim) ou N (para não).')


        case 2:
            print('-='*20)
            print('SOLICITAR CADASTRO DE CONDOMÍNIO')
            print('-='*20)

            print('Insira as informações requisitadas abaixo, acerca do condomínio:')
            condominio['estado'] = str(input('Estado: '))
            condominio['municipio'] = str(input('Município: '))
            condominio['bairro'] = str(input('Bairro: '))
            condominio['ruav'] = str(input('Rua/avenida: '))
            condominio['numero'] = str(input('Número: '))
            condominio['nomeCondo'] = str(input('Nome do condomínio: '))
            
            print('Agora, insira as informações requisitadas abaixo, acerca de você:')
            condominio['nomeGestor'] = str(input('Seu nome: '))
            condominio['cargoGestor'] = str(input('Cargo/função: '))
            condominio['emailGestor'] = str(input('Por último, seu e-mail:'))
            
            print(f'Solicitação recebida com sucesso! Obrigado pela confiança, {condominio['nomeGestor']}!')
            print('O código do seu condomínio será enviado para seu e-mail dentro de 1 semana!')
            print('Para acessar e gerenciar o seu condomínio, volte ao menu, selecione a opção 1 e insira o código informado!')

            # Voltar ao menu
            voltar = str(input('Digite M para voltar ao menu -> ')).upper
            while voltar not in ("M"):
                print('Caracter inválido! Por favor, tente novamente.')
                voltar = str(input('Digite M para voltar ao menu -> ')).upper
            
            if voltar in 'M':
                main()


        case 3:
            print('Remover um condomínio cadastrado')

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
