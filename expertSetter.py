T = int(input())

for i in range(T):
    X,Y = map(int, input().split())
    ok = X / 2
    if Y >= ok:
        print('YES')
    else:
        print('NO')
