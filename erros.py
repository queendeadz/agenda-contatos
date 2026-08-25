# erros em tempo de compliação
# erros em tempo de execução
# erros de logica

def divisao(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('Divisao invalida')
        print(e)

divisao(20,10)