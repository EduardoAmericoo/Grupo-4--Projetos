import json

def obter_proximo_id():
    file = 'database/chat.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read() 
        data = json.loads(read)
        
        ids = [int(row['id_mensagem']) for row in data]
        return max(ids) + 1 if ids else 1

def cadastrarMensagem(id, nome_emissor, mensagem):
    file = 'database/chat.json'
    
    msg = {
        "id_mensagem": id,
        "nome_emissor": nome_emissor,
        "mensagem": mensagem
    }
    
    mensagem_cadastrada = False

    with open(file, 'r', encoding='utf8') as arquivo:
        mensagens = json.load(arquivo)
    
    mensagens.append(msg)
    
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(mensagens, indent=4))
        
        mensagem_cadastrada = True
    
    return mensagem_cadastrada

def atualizarMensagem(msg_to_update):
    file = 'database/condominios.json'
    msg_updated = False
        
    mensagem = buscarMensagem()
    for c in mensagem:
        if msg_to_update == c['mensagem'].upper():
            c['mensagem'] = str(input("Mensagem: "))         
        
            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(mensagem, indent=4))
        
                msg_updated = True
            break
    
    return msg_updated
    
def deletarMensagem(msg_to_delete):
    file = 'database/chat.json'
    msg_deleted = False
    new_list = []

    mensagens = buscarMensagem()
    for c in mensagens:
        if msg_to_delete != c['mensagem'].upper():
            new_list.append(c)
    
    msg = new_list 

    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(msg, indent=4))
        
        msg_deleted = True
    
    return msg_deleted

def buscarMensagem():
    file = 'database/chat.json'
    
    with open(file, 'r', encoding='utf8') as usuario:
        read = usuario.read() 
        data = json.loads(read) 
            
    return data
    