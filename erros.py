# erros em tempo de compliação
# erros em tempo de execução
# erros de logica

try:
        a = float(input('Digite o numero A: '))
        b = float(input('Digite o numero B: '))

        print(a/b)

except ValueError as e:
        print('Input invalido, digite apenas numeros')
except ZeroDivisionError as e:
    print('Não pode ser feita divisão por zero')
except Exception as e:
    print('Algum erro ocorreu')
    print(e)
finally:
    print('Fim do programa')

