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