import re
N = int(input())

for i in range(N):
    letra = str(input())
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    padrao = f'[{consoantes}]{{3,}}'
    busca = re.search(padrao, letra)

    if busca:
        print(f"{letra} nao eh facil")
    else:
        print(f"{letra} eh facil")
