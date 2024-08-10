t = int(input())
limite = [x for x in range(10,20)]
contador = 0
fora = 0

for i in range(t):
    x = int(input())
    if x in limite:
        contador += 1
    else:
        fora += 1
        
print(f"{contador} in")
print(f"{fora} out")
