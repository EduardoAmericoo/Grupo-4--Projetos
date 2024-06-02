import json

def obter_proximo_id():
    file = 'database/condominios.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read() 
        data = json.loads(read)
        
        ids = [int(row['id']) for row in data]
        return max(ids) + 1 if ids else 1

# Cadastrar Condomínio
def cadastrarCondominio(id, nome_cond, endereco, cep, qntd_andares, qntd_apto):
    file = 'database/condominios.json'
    
    # cria objeto para escrever
    cond = {
        "id": id,
        "nome": nome_cond,
        "endereco": endereco,
        "cep": f"{cep[:5]}-{cep[5:]}",
        "qntd_andares": qntd_andares,
        "qntd_apto": qntd_apto 
    }
    
    condominio_cadastrado = False
    # abre o arquivo e carrega o conteúdo
    with open(file, 'r', encoding='utf8') as arquivo:
        condominios = json.load(arquivo)
    
    # adiciona o novo cadastro na lista    
    condominios.append(cond)
    
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(condominios, indent=4))
        
        condominio_cadastrado = True
    
    return condominio_cadastrado

# Atualizar Condomínio
def atualizarCondominio(cond_to_update):
    file = 'database/condominios.json'
    cond_updated = False
    
    # listar condomínios e dados existentes 
    
    condominios = buscarCondominio()
    for c in condominios:
        if cond_to_update == c['id']:
            c['nome'] = str(input("Novo nome: "))      
            c['qntd_andares'] = str(input("Quantidade de andares: "))          
            c['qntd_apto'] = str(input("Quantidade de apartamentos: "))      
        
            # escrever em arquivos json
            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(condominios, indent=4))
        
                cond_updated = True
            break
    
    return cond_updated
    
# Deletar Condomínio
def deletarCondominio(cond_to_delete):
    file = 'database/condominios.json'
    cond_deleted = False
    new_list = []

    # Verifica todos os registros que não batem com o nome e adiciona em uma lista
    condominios = buscarCondominio()
    for c in condominios:
        if cond_to_delete != c['id']:
            new_list.append(c)
    
    conds = new_list 
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(conds, indent=4))
        
        cond_deleted = True
    
    return cond_deleted

# Buscar Condomínio
def buscarCondominio():
    file = 'database/condominios.json'
    
    with open(file, 'r') as usuario:
        read = usuario.read() 
        data = json.loads(read) 
            
    return data

# FORMATAÇÕES DE CEP 
def formatarCEP(cep):
    cep_cadastrado = False
    condominios = buscarCondominio()

    for c in condominios:
        if cep == c['cep']:
            cep_cadastrado = True
        break

    while len(cep) != 8 or not cep.isdigit() or cep == "" or cep_cadastrado:
        if cep == "": 
            print("Campo obrigatório!")
        elif len(cep) != 8:
            print("Campo deve conter 8 caracteres.")
        elif not cep.isdigit():
            print("O CEP deve conter apenas digitos numéricos.")
        elif cep_cadastrado:
            print(f"O CEP '{cep}' já está cadastrado.")

        cep = str(input("Digite seu CEP: "))
        
        return cep 
