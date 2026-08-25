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


def buscar_contato(contato):
    print('nome: ', contato)
    print("telefone:", AGENDA[contato]["telefone"])
    print("email:", AGENDA[contato]["email"])
    print("endereco:", AGENDA[contato]["endereco"])
    print("----------------------------")
    print()



def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    "telefone": telefone,
    "email": email,
    "endereco": endereco,
    }
    print()
    print('====== Contato {} adicionado/editado com sucesso ======'.format(contato))
    print()


def excluir_contato(contato):
    AGENDA.pop(contato)
    print()
    print('====== Contato {} removido com sucesso ======'.format(contato))
    print()


def imprimir_menu():
    print("----------------------------")
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')
    print("----------------------------")

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o numero de telefone: ')
        email = input('Digite o email do contato: ')
        endereco = input('Digite o endereco do contato: ')
        incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '0':
        print('Fechando agenda')
        break
    else:
        print('Opção invalida!')
        print()


