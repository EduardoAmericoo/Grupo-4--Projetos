import csv

usuarios = list()

def obter_proximo_id():
    try:
        with open('database/usuarios.csv', mode='r') as file:
            reader = csv.DictReader(file)
            ids = [int(row['id']) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1
    
def cadastrarUsuario(id, tipo_user, nome, cpf, senha, email, telefone, apartamento):
    usuario_cadastrado = False
    # escrever em arquivos csv
    with open('database/usuarios.csv', 'a', newline='') as arquivo:
        # cria objeto para escrever
        escrever = csv.writer(arquivo)
        
        # escreve no arquivo linha a linha
        escrever.writerow((id, tipo_user, nome, cpf, senha, email, telefone, apartamento))
        
        usuario_cadastrado = True
    
    return usuario_cadastrado

def buscarUsuario():
    global usuarios
    
    with open('database/usuarios.csv', 'r', encoding='utf8') as usuario:
        reader = csv.DictReader(usuario)
        
        for row in reader:
            usuarios.append(row.copy())
            
    return usuarios

def listarUsuario(nome):
    with open('database/usuarios.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        result = []
        for row in reader:
            if nome.upper() in row[2].upper():
                result.append(row)
        
        return result

def atualizarUsuario():
    print("Atualizar")
    
def deletarUsuario():
    print("Deletar")

def autenticar_usuario(cpf, senha):
    global id_user, nome_user, cpf_user, senha_user, email_user, telefone_user, apto_user
    
    usuarios = buscarUsuario()
    for u in usuarios:
        if cpf in u['cpf'] and senha in u['senha']:
            id_user = u['id']
            nome_user = u['nome']
            cpf_user = u['cpf']
            senha_user = u['senha']
            email_user = u['email']
            telefone_user = u['telefone']
            apto_user = u['apartamento']
            
            usuario_autenticado = True
            return usuario_autenticado
        else:
            usuario_autenticado = False
            return usuario_autenticado
