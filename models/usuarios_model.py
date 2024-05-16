import json

# Obtém o próximo ID
def obter_proximo_id():
    file = 'database/usuarios.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read() # ler os dados como texto
        data = json.loads(read) # carregar os dados no formato json
        
        ids = [int(row['id']) for row in data]
        return max(ids) + 1 if ids else 1

# Cadastrar Usuário
def cadastrarUsuario(id, is_adm, nome, cpf, senha, email, telefone, apartamento):
    file = 'database/usuarios.json'
    
    # cria objeto para escrever
    user = {
        "id": id,
        "is_adm": is_adm,
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "email": email,
        "telefone": telefone,
        "apartamento": apartamento   
    }
    
    usuario_cadastrado = False
    # abre o arquivo e carrega o conteúdo
    with open(file, 'r', encoding='utf8') as arquivo:
        usuarios = json.load(arquivo)
    
    # adiciona o novo usuário na lista    
    usuarios.append(user)
    
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(usuarios, indent=4))
        
        usuario_cadastrado = True
    
    return usuario_cadastrado

# Atualizar Usuários
def atualizarUsuario():
    print("Atualizar")
    
# Atualizar Usuários
def deletarUsuario():
    print("Deletar")

# Buscar Usuários
def buscarUsuario():
    file = 'database/usuarios.json'
    
    with open(file, 'r') as usuario:
        read = usuario.read() # ler os dados como texto
        data = json.loads(read) # carregar os dados no formato json
            
    return data

# Autenticar Usuários
def autenticar_usuario(cpf, senha):
    global id_user, is_adm, nome_user, cpf_user, senha_user, email_user, telefone_user, apto_user
    
    users = buscarUsuario()
    for u in users:
        global user, password
        user = cpf
        password = senha
    
        if cpf == u['cpf'] and senha == u['senha']:
            id_user = u['id']
            is_adm = u['is_adm']
            nome_user = u['nome']
            cpf_user = u['cpf']
            senha_user = u['senha']
            email_user = u['email']
            telefone_user = u['telefone']
            apto_user = u['apartamento']
            
            usuario_autenticado = True
            return usuario_autenticado
        
    usuario_autenticado = False
    return usuario_autenticado
