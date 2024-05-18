import json
import menu_adm

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

# Buscar Usuários
def buscarUsuario():
    file = 'database/usuarios.json'
    
    with open(file, 'r') as usuario:
        read = usuario.read() # ler os dados como texto
        data = json.loads(read) # carregar os dados no formato json
            
    return data

# Atualizar Usuários
def atualizarUsuario(is_adm, nome, cpf, senha, email, telefone, apartamento):
    file = 'database/usuarios.json'
    with open(file, 'r') as usuario:
        read = usuario.read()
        data = json.loads(read)
        print(data)
        
    while True:
        usuarioAtualizado = False
        userAtt = str(input('Informe o usuário que deseja atualizar: ')).upper()
        user = {}

        for c in buscarUsuario():
            print(f'{c['id']} - {c['nome']}')
            if menu_adm.userAtt == c['nome'].upper():
                
                is_adm = str(input("Administrador? [S/N]: ")).upper()
                formatarADM(is_adm)
                
                nome = str(input("Novo nome: "))
                formatarNome(nome)

                cpf = str(input('Novo CPF: '))
                formatarCPF(cpf)
                
                senha = str(input("Nova senha: "))
                formatarSenha(senha)
                    
                email = str(input("Novo email: "))
                formatarEmail(email)

                telefone = str(input("Novo telefone: "))
                formatarTelefone(telefone)

                apartamento = str(input("Novo apartamento: "))
                formatarApartamento(apartamento)
                
                usuarioAtualizado = usuario.atualizarUsuario(nome, senha, is_adm, email, telefone, apartamento)

                user = {
                    "id": c['id'],
                    "is_adm": is_adm,
                    "nome": nome,
                    "cpf": cpf,
                    "senha": senha,
                    "email": email,
                    "telefone": telefone,
                    "apartamento": apartamento   
                }
                break
            
            # adiciona o novo usuário no dicionário
            buscarUsuario().insert(c['id'], user)

            # escrever em arquivos json
            with open(file, 'w', encoding='utf8') as arquivo:
                arquivo.write(json.dumps(userAtt, indent=4))
                
                usuarioAtualizado = True
        
        return usuarioAtualizado
    
# Atualizar Usuários
def deletarUsuario():
    print("Deletar")

# Autenticar Usuários
def autenticar_usuario(cpf, senha):
    global id, is_adm, nome, email, telefone, apartamento
    
    users = buscarUsuario()
    for u in users:
        global user, password
        user = cpf
        password = senha
    
        if cpf == u['cpf'] and senha == u['senha']:
            id = u['id']
            is_adm = u['is_adm']
            nome = u['nome']
            cpf = u['cpf']
            senha = u['senha']
            email = u['email']
            telefone = u['telefone']
            apartamento = u['apartamento']
            
            usuario_autenticado = True
            return usuario_autenticado
        
    usuario_autenticado = False
    return usuario_autenticado

# FORMATAÇÕES DE CPF, SENHA E ADMNINISTRAÇÃO PARA CADASTRO E UPDATE DE USUÁRIOS 
def formatarADM(is_adm):

    while is_adm != "S" and is_adm != "N":
        if is_adm == "":
            print("Campo obrigatório!")
        else:
            print("Resposta inválida. Por favor, use apenas 'S' ou 'N'.")
        is_adm = str(input('Administrador? [S/N]: ')).upper()

    if is_adm == "S":
        is_adm = True

    if is_adm == "N":
        is_adm = False
    
def formatarNome(nome):
    while nome == "":
        print("Campo obrigatório!")
        nome = str(input('Nome: '))

def formatarCPF(cpf):
    while len(cpf) != 11:
        if cpf == "":
            print("Campo obrigatório!")
        else:
            print("Campo deve conter 11 caracteres.")
        cpf = str(input('CPF: '))
    
    while not cpf.isdigit():
        print("O cpf deve conter apenas digitos numéricos.")
        cpf = str(input("CPF: "))

def formatarSenha(senha):
    while len(senha) < 8:
        if senha == "":
            print("Campo obrigatório!")
        else:
            print("A senha deve ter, no mínimo, 8 caracteres!")
        senha = str(input('Senha: '))

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

def verificarCPFCadastrado():
    print("CPF já cadastrado!")