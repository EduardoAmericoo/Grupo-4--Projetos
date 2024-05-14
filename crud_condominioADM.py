import os

def menuGAdm():
    print('='*35)
    print('GERENCIAMENTO DE CONDOMÍNIO (ADM)')
    print('='*35)

    print('1 - Gerenciar condomínio')
    print('2 - Remover seu condomínio')
    print('0 - Voltar ao menu de cadastro')
    
def choiceGAdm():    
    opcao = int(input('Digite uma opção: '))

    match (opcao):

        case 1:
            print('-='*20)
            print('GERENCIAR CONDOMÍNIO')
            print('-='*20)

            print('Opções de acesso:')
            print('1 - Acessar o cadastro de moradores')
            print('2 - Acessar chat de comunicação')
            print('3 - Acessar página de reserva de áreas comuns')
            print('0 - Voltar ao menu de ações')
            
            opcaoGAdm = int(input('Escolha a ação a ser tomada -> ')

            match (opcaoGAdm){
                case 1:
                    #PAGINA DE CADASTRAR MORADOR
                case 2: 
                    #PAGINA DE CHATS
                case 3:
                    #PAGINA DE AREAS COMUNS
                case 0:
                    print('Voltando...')
                    #PUXAR MENU ANTERIOR
                case __:
                    print('Opção inválida! Tente novamente.')
                    mainGAdm()
                
        case 2:
            print('-='*20)
            print('REMOVER O SEU CONDOMÍNIO CADASTRADO')
            print('-='*20)

            confirmacao = str(input(f'Deseja excluir do cadastro o condomínio {condominio}? (S/N)').upper
            if confirmacao == 'S':
                del condCadastrado
            elif confirmacao == 'N':
                
            
        case 0:
            #CHAMAR O MENU ANTERIOR

        case __:
            print('Opção inválida! Tente novamente.')
            mainGAdm()

def mainGAdm():
    os.system('cls')
    menuGAdm()
    choiceGAdm()

if __name__ == '__main__':
    main()
