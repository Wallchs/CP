testecase = int(input())

for _ in range(testecase):
    scores = []
    for i in range(22):
        a, b = map(int, input().split())
        score = a + b * 20 - 128
        scores.append(score)

    man_of_the_match = scores.index(max(scores)) + 1
    print(man_of_the_match)

