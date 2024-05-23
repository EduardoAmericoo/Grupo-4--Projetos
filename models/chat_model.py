import json

# Obtém o próximo ID
def obter_proximo_id():
    file = 'database/chat.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read() 
        data = json.loads(read)
        
        ids = [int(row['id_mensagem']) for row in data]
        return max(ids) + 1 if ids else 1

# Cadastrar Condomínio
def cadastrarMensagem(id, nome_emissor, mensagem):
    file = 'database/chat.json'
    
    # cria objeto para escrever
    msg = {
        "id_mensagem": id,
        "nome_emissor": nome_emissor,
        "mensagem": mensagem
    }
    
    mensagem_cadastrada = False
    # abre o arquivo e carrega o conteúdo
    with open(file, 'r', encoding='utf8') as arquivo:
        mensagens = json.load(arquivo)
    
    # adiciona o novo cadastro na lista    
    mensagens.append(msg)
    
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(mensagens, indent=4))
        
        mensagem_cadastrada = True
    
    return mensagem_cadastrada

# Atualizar Condomínio
def atualizarMensagem(cond_to_update):
    file = 'database/condominios.json'
    cond_updated = False
    
    # listar condomínios e dados existentes 
    
    condominios = buscarCondominio()
    for c in condominios:
        if cond_to_update == c['nome'].upper():
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
def deletarMensagem(msg_to_delete):
    file = 'database/chat.json'
    msg_deleted = False
    new_list = []

    # Verifica todos os registros que não batem com o nome e adiciona em uma lista
    mensagens = buscarMensagem()
    for c in mensagens:
        if msg_to_delete != c['mensagem'].upper():
            new_list.append(c)
    
    msg = new_list 
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(msg, indent=4))
        
        msg_deleted = True
    
    return msg_deleted

# Buscar Condomínio
def buscarMensagem():
    file = 'database/chat.json'
    
    with open(file, 'r', encoding='utf8') as usuario:
        read = usuario.read() 
        data = json.loads(read) 
            
    return data
    