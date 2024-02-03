T = int(input())

for i in range(T):
    n = int(input())
    soma = n * (n + 1) / 2
    if soma % 2 == 0:
        print(n)
    else:
        print(n - 1)
