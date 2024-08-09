num = list(map(int, input().split()))
num2 = num.copy()
num.sort()

for i in range(len(num)):
	print(num[i])

print("")

for i in range(len(num2)):
	print(num2[i])
