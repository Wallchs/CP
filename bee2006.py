T = int(input())

A, B, C, D, E = map(int, input().split())

arr = [A, B, C, D, E]

novoarr = []
for i in range(len(arr)):
    if arr[i] == T:
        novoarr.append(i)

print(len(novoarr))
