import json

def obter_proximo_id():
    file = 'database/usuarios.json'
    
    with open(file, mode='r') as arquivo:
        read = arquivo.read()
        data = json.loads(read)
        
        ids = [int(row['id']) for row in data]
        return max(ids) + 1 if ids else 1

def cadastrarUsuario(id, is_adm, nome, cpf, senha, email, telefone, apartamento):
    file = 'database/usuarios.json'

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
    with open(file, 'r', encoding='utf8') as arquivo:
        usuarios = json.load(arquivo)
    
    usuarios.append(user)
    
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(usuarios, indent=4))
        
        usuario_cadastrado = True
    
    return usuario_cadastrado

def atualizarUsuario(user_to_update):
    file = 'database/usuarios.json'
    user_updated = False
    user = {}
    
    users = buscarUsuario()
    for c in users:
        if user_to_update == c['id']:
            c['nome'] = str(input("Novo nome: "))
                    
            c['senha'] = str(input("Nova senha: "))
            formatarSenha(c['senha'])
                        
            is_adm = str(input("Usuário é adm: [S/N] ")).upper()
            c['is_adm'] = formatarADM(is_adm)
                       
            c['email'] = str(input("Novo email: "))      
            c['telefone'] = str(input("Novo telefone: "))
            c['apartamento'] = str(input("Novo apartamento: "))

            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(users, indent=4))
        
            user_updated = True
            break
    
    return user_updated

def atualizarUsuarioMorador(user_to_update):
    file = 'database/usuarios.json'
    user_updated = False
    user = {}
    
    users = buscarUsuario()
    for c in users:
        if user_to_update == c['id']:
            c['nome'] = str(input("Novo nome: "))
                    
            c['senha'] = str(input("Nova senha: "))
            formatarSenha(c['senha'])
                       
            c['email'] = str(input("Novo email: "))      
            c['telefone'] = str(input("Novo telefone: "))
            c['apartamento'] = str(input("Novo apartamento: "))

            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(users, indent=4))
        
                user_updated = True
            break
    
    return user_updated
    
def deletarUsuario(user_to_delete):
    file = 'database/usuarios.json'
    user_deleted = False
    new_list = []

    users = buscarUsuario()
    for c in users:
        if user_to_delete != c['id']:
            new_list.append(c)
    
    users = new_list
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(users, indent=4))
        
        user_deleted = True
    
    return user_deleted

def buscarUsuario():
    file = 'database/usuarios.json'
    
    with open(file, 'r') as usuario:
        read = usuario.read()
        data = json.loads(read)
            
    return data

def listar_informacoes_usuario(data, id):
    for usuario in data['usuarios']:
        if usuario['id'] == id:
            return usuario
    return None

def autenticar_usuario(cpf, senha):
    global id_user, is_adm, nome_user, cpf_user, senha_user, email_user, telefone_user, apto_user
    usuario_autenticado = False
    
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

def dadosUsuarioAutenticado(cpf):
    users = buscarUsuario()
    for u in users:
        if cpf == u['cpf']:
            return u

def formatarADM(is_adm):

    while is_adm not in "SN":
        print("Campo obrigatório! Use apenas 'S' ou 'N'.")
        
        is_adm = str(input("Administrador? [S/N]: ")).upper()
                    
    if is_adm == "S":
        is_adm = True
    else:
        is_adm = False
    
    return is_adm

def formatarNome(nome):
    while nome == "":
        print("Campo obrigatório!")
        
        nome = str(input('Nome: '))

def formatarCPF(cpf):
    cpf_cadastrado = False
    users = buscarUsuario()

    for c in users:
        if cpf == c['cpf']:
            cpf_cadastrado = True
        break
    
    while len(cpf) != 11 or not cpf.isnumeric() or cpf_cadastrado:
        if len(cpf) != 11: 
            print("Este campo é obrigatório e deve conter 11 dígitos numéricos.")
        elif not cpf.isnumeric():
            print("Campo deve conter apenas dígitos numéricos.")
        elif cpf_cadastrado:
            print(f"O CPF '{cpf}' já está cadastrado.")

        cpf = str(input("CPF: "))

def formatarSenha(senha):
    while len(senha) < 5:
        if senha == "" or len(senha) < 5:
            print("Este campo é obrigatório e deve conter no mínimo 5 caracteres!")

        senha = str(input("Digite seu senha: "))
    
def formatarEmail(email):
    while email == "":
        print("Campo obrigatório!")
        
        email = str(input('E-mail: '))

def formatarTelefone(telefone):
    while telefone == "":
        print("Campo obrigatório!")
        
        telefone = str(input('Telefone: '))

def formatarApartamento(apartamento):
    while apartamento == "":
        print("Campo obrigatório!")
        
        apartamento = str(input('Apartamento: '))
