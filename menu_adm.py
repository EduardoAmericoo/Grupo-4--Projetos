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
    
def opcoes_adm(opc):
    while opc not in ("123456"):
        print("Opção inválida, Tente novamente")
        opc = str(input("Digite a opção: "))   
    
    match(opc):
        case "1": 
            # Gerenciar Usuários
            print(opc)
        case "2":
            # Gerenciar condomínios 
            print(opc)
        case "3": 
            # Gerenciar áreas comuns
            print(opc)
        case "4": 
            # Gerenciar reservas
            print(opc)
        case "5": 
            # Comunicação
            print(opc)
        case "6": 
            print("Saindo...")
        case __:
            print(opc, "Errou")      