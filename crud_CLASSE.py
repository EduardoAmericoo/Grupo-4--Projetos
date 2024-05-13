import os
from random import randint

condominio = dict(list)
condsCadastrados = list()

def menu():
    print('-='*7)
    print('IDENTIFICAÇÃO')
    print('-='*7)

    print('1 - Fazer login')
    print('2 - Obter ID (novo na ferramenta)')
    print('0 - Sair')

def choice():
    opcao = int(input('Insira o número aqui -> '))

    match (opcao):
        case 1:
            print('-='*4)
            print('LOGIN - MORADOR/GESTOR')
            print('-='*4)

            id = str(input('Insira o ID do condomínio -> ')
            classe = str(input('Insira o seu CPF -> ')
            #PUXAR FUNÇÃO DA PAGINA INICIAL MORADOR/GESTOR
        
        case 2:
            print('-='*15)
            print('CADASTRAR NA PLATAFORMA E OBTER ID')
            print('Apenas gestores e síndicos')
            print('-='*15)
                     
            print('Insira suas informações requisitadas abaixo:')
            condominio['nomeGestor'] = str(input('Nome: '))
            condominio['cargoGestor'] = str(input('Cargo/função: '))
            condominio['emailGestor'] = str(input('E-mail: '))
            condominio['cpfGestor] = str(input('CPF: '))
                     
            print('Insira as informações requisitadas abaixo, acerca do condomínio:')
            condominio['estado'] = str(input('Estado: '))
            condominio['municipio'] = str(input('Município: '))
            condominio['bairro'] = str(input('Bairro: '))
            condominio['ruav'] = str(input('Rua/avenida: '))
            condominio['numero'] = str(input('Número: '))
            condominio['nomeCondo'] = str(input('Nome do condomínio: '))

            condsCadastrados.append(condominio.copy())

            '''opcao 1
            codigo = randint(1000, 9999)
            print(f'O código do seu condomínio é {codigo})
            print('Guarde e envie para os moradores, pois é com ele que poderão fazer login.')'''

            '''opcao 2
            with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            ids = [int(row['ID']) for row in reader]
            return max(ids) + 1 if ids else 1
            except FileNotFoundError:
            return 1'''
        case 0:
            print('Saindo...')
        case __:
            print('Opção inváida! Por favor, tente novamente.')
            main()

def main():
    os.system('cls')
    menu()
    choice()

if __name__ == '__main__':
    main()
