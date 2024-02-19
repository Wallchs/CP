
dados = list(map(float, input().split()))
dados2 = list(map(float, input().split()))


resultado = (dados[1] * dados[2]) + (dados2[1] * dados2[2])


print(f"VALOR A PAGAR: R$ {resultado:.2f}")
