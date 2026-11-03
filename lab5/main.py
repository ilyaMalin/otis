from itertools import combinations

listAlternative = ["Матпомощь", "Курсы", "Путёвка"]
listRank = [
    ["Матпомощь", "Курсы", "Путёвка"],
    ["Курсы", "Путёвка", "Матпомощь"],
    ["Матпомощь", "Курсы", "Путёвка"],
]

size = len(listAlternative)
preference = [["—" if i == j else 0 for j in range(size)] for i in range(size)]

for alt1, alt2 in combinations(listAlternative, 2):
    i = listAlternative.index(alt1)
    j = listAlternative.index(alt2)

    for rank in listRank:
        if rank.index(alt1) < rank.index(alt2):
            preference[i][j] += 1
        else:
            preference[j][i] += 1

print("Матрица предпочтений")
for row in preference:
    print(row)

print("Попарное сравнение альтерантив:")
for i in range(size):
    for j in range(i + 1, size):
        res = None
        if preference[i][j] > preference[j][i]:
            res = listAlternative[i]
        elif preference[i][j] < preference[j][i]:
            res = listAlternative[j]
        else:
            res = "Ничья"

        print(f"{listAlternative[i]} ({preference[i][j]}) V {listAlternative[j]} ({preference[j][i]}) —> {res}")

winner = None
for i in range(size):
    if all(preference[i][j] > preference[j][i] for j in range(size) if i != j):
        winner = listAlternative[i]
        break

if winner:
    print(f"Наилучший выбор — {winner}")
else:
    print("Не удалось определить альтернативу!")
