
testecase = int(input())

while testecase > 0:
    NumberofJudges = int(input())

    arr = list(map(int, input().split()))
    all_good = True

    for j in range(len(arr)):
        if arr[j] <= 4:
            all_good = False
            break

    if all_good:
        print("YES")
    else:
        print("NO")

    testecase -= 1

    

