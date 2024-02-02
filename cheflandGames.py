T = int(input())

for i in range(T):
    r1,r2,r3,r4 = list(map(int, input().split()))
    mylist = [r1,r2,r3,r4]
    if mylist.count(0) == 4:
        print("IN")
    else:
        print("OUT")
