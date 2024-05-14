# IMPORTANDO FRAMEWORKS
import os
from random import randint

# IMPORTANDO CSV
import csv

condominio = dict(list)
condsCadastrados = list()

def menu():
    print('-='*7)
    print('IDENTIFICAÇÃO')
    print('-='*7)

    print('1 - Fazer login')
    print('2 - Fazer cadastro como gestor')
    print('3 - Fazer cadastro de condomínio')
    print('0 - Sair')

def choice():
    opcao = int(input('Insira o número aqui -> '))

    match (opcao):
        case 1:
            print('-='*4)
            print('LOGIN - MORADOR/GESTOR')
            print('-='*4)

            idCondo = str(input('Insira o ID do condomínio -> '))
            classe = str(input('Insira o seu CPF -> '))
            #MENSAGEM DE BOAS VINDAS
            #PUXAR FUNÇÃO DA PAGINA INICIAL MORADOR/GESTOR
        
        case 2:
            print('nada')
        
        case 3:
            print('-='*15)
            print('CADASTRO - CONDOMÍNIO')
            print('Apenas gestores e síndicos')
            print('-='*15)
                     
            print('Insira as informações requisitadas abaixo, acerca do condomínio:')
            condominio['estado'] = str(input('Estado: '))
            condominio['municipio'] = str(input('Município: '))
            condominio['bairro'] = str(input('Bairro: '))
            condominio['ruav'] = str(input('Rua/avenida: '))
            condominio['numero'] = str(input('Número: '))
            condominio['nomeCondo'] = str(input('Nome do condomínio: '))

            condsCadastrados.append(condominio.copy())

            codigo = randint(1000, 9999)
            print(f'O código do seu condomínio é {codigo}')
            print('Guarde e envie para os moradores. É com ele que poderão fazer login.')

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
