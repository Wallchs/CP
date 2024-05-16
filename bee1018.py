notas = [100, 50, 20, 10, 5, 2, 1]


def decompor_valor_em_notas(valor):
    quantidade_notas = [0, 0, 0, 0, 0, 0, 0]

    for i, nota in enumerate(notas):
        while valor >= nota:
            valor -= nota
            quantidade_notas[i] += 1

    return quantidade_notas


valor = int(input())

quantidade_notas = decompor_valor_em_notas(valor)

print(valor)
for i, quantidade in enumerate(quantidade_notas):
    print(f'{quantidade} nota(s) de R$ {notas[i]},00')
