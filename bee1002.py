
def calculaRaio(raio):
    pi = 3.14159
    return f'A={pi * (raio ** 2.0):.4f}'


numero = float(input())

print(calculaRaio(numero))
