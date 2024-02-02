T = int(input())

for i in range(T):
    A,B,X,Y = map(int, input().split())
    parA = A * B
    parB = X * Y
    if parB >= parA:
        print("Yes")
    else:
        print("No")
