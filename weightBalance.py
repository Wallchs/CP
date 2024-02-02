T = int(input())
for i in range(T):
    w1,w2,x1,x2,M = list(map(int, input().split()))
    correctVal = 2
    mylist = [w2,w1]
    result = mylist[0] - mylist[1]
    if (result >= correctVal and result > 4):
        print("1")
    else:
        print("0")
