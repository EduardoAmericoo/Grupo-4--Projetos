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
def atualizarUsuario(user_to_update):
    file = 'database/usuarios.json'
    user_updated = False
    user = {}
    
    users = buscarUsuario()
    for c in users:
        if user_to_update == c['nome'].upper():
            c['nome'] = str(input("Novo nome: "))
                    
            c['senha'] = str(input("Nova senha: "))
            formatarSenha(c['senha'])
                        
            c['is_adm'] = str(input("Usuário é adm: [S/N] ")).upper()
            formatarADM(c['is_adm'])
                       
            c['email'] = str(input("Novo email: "))      
            c['telefone'] = str(input("Novo seu telefone: "))
            c['apartamento'] = str(input("Novo seu apartamento: "))
        
            # escrever em arquivos json
            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(users, indent=4))
        
                user_updated = True
            break
    
    return user_updated
    
# Deletar Usuários
def deletarUsuario(user_to_delete):
    file = 'database/usuarios.json'
    user_deleted = False
    new_list = []

    # Verifica todos os registros que não batem com o nome e adiciona em uma lista
    users = buscarUsuario()
    for c in users:
        if user_to_delete != c['nome'].upper():
            new_list.append(c)
    
    users = new_list 
    # escrever em arquivos json
    with open(file, 'w', encoding='utf8') as arquivo:
        arquivo.write(json.dumps(users, indent=4))
        
        user_deleted = True
    
    return user_deleted

# Buscar Usuários
def buscarUsuario():
    file = 'database/usuarios.json'
    
    with open(file, 'r') as usuario:
        read = usuario.read() # ler os dados como texto
        data = json.loads(read) # carregar os dados no formato json
            
    return data

def listar_informacoes_usuario(data, id):
    for usuario in data['usuarios']:
        if usuario['id'] == id:
            return usuario
    return None

# Autenticar Usuários
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

# FORMATAÇÕES DE CPF, SENHA E ADMNINISTRAÇÃO PARA CADASTRO E UPDATE DE USUÁRIOS 
def formatarADM(is_adm):

    while is_adm not in "SN":
        print("Campo obrigatório! Use apenas 'S' ou 'N'.")
        
        is_adm = str(input("Administrador? [S/N]: ")).upper()
                    
        if is_adm == "S":
            is_adm = True
        else:
            is_adm = False

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