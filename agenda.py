AGENDA = {}

AGENDA ["sarah"] = {
    "telefone": "1195763122",
    "email": "sarah@gmail.com",
    "endereco": "avenida n1",
}
AGENDA ["maria"] = {
    "telefone": "1195333322",
    "email": "maria@gmail.com",
    "endereco": "avenida n2",
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print ("=================")


def buscar_contato(contato):
    print('Nome: ', contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("Email:", AGENDA[contato]["email"])
    print("Endereco:", AGENDA[contato]["endereco"])


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    "telefone": telefone,
    "email": email,
    "endereco": endereco,
    }
    print('====== Contato {} adicionado com sucesso ======'.format(contato))

#buscar_contato("abel")
incluir_contato('abel', '1138462384632', 'abel@gmail.com', 'avenida n3')
mostrar_contatos()



