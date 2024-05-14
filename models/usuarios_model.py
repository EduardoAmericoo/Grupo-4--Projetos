import csv

usuarios = list() 

def buscarUsuario():
    global usuarios
    
    with open('database/usuarios.csv', 'r', encoding='utf8') as usuario:
        reader = csv.DictReader(usuario)
        
        for row in reader:
            usuarios.append(row.copy())
            
    return usuarios

def autenticar_usuario(cpf, senha):
    global id_user, nome_user, cpf_user, senha_user, email_user, telefone_user, apto_user
    
    usuarios = buscarUsuario()
    for u in usuarios:
        if cpf in u['cpf'] and senha.upper() in u['senha'].upper():
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
