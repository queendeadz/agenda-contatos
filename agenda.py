AGENDA = {}

AGENDA ["sarah"] = {
    "telefone": "1195763122",
    "email": "sarah@gmail.com",
    "endereco": "avenida das avenidas n 999",
}
AGENDA ["maria"] = {
    "telefone": "1195333322",
    "email": "maria@gmail.com",
    "endereco": "avenida n 999",
}

def mostrar_contatos():
    for contato in AGENDA:
        print ("Nome:", contato)
        print("Telefone:", AGENDA[contato] ["telefone"])
        print("Email:", AGENDA[contato] ["email"])
        print("Endereco:", AGENDA[contato] ["endereco"])

        print ("===========")

mostrar_contatos()