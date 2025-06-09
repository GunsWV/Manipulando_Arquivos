arquivo = open("pessoa.txt", "w", encoding="utf-8")
arquivo.write("CADASTROS!\n")
arquivo.close()

while True:

    print("Olá, somos do sistema de cadastro, Tudo bem?\nDigite aqui seu nome e seu email, Por gentileza")

    nome_usuario = input("Digite aqui o seu nome:")
    email_usuario = input("Digite aqui seu email:")

    arquivo = open('pessoa.txt', 'a', encoding='utf-8')
    arquivo.write(f"Pessoa/Usuário: {nome_usuario} \n")
    arquivo.write(f"Email do Usuário: {email_usuario} \n")
    arquivo.close()

    arquivo = open("pessoa.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()
    print("Até o momento os usuários cadastrados são:")
    print(conteudo)
    arquivo.close()


    final = input("Se quiser cadastrar outro nome digite continuar \n ou \nDigite voltar para sair:")

    if final == "voltar":
        break

         