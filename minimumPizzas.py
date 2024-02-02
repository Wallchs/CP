T = int(input())
for i in range(T):
    N,X = map(int, input().split())
    pizzas = N * X // 4
    if N * X % 4 == 0:
        print(pizzas)
    else:
        print(pizzas + 1)
