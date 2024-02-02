T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    if K == 0:
        print(N)
    else:
        print(N % K)
    






