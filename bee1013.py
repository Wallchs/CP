a,b,c = map(int, input().split())
formula = (a+b+abs(a-b)) / 2
maior = (formula+c+abs(formula-c)) / 2
print(f"{maior:.0f} eh o maior")
