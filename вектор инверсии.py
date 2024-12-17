
vector = [0, 0, 0, 3, 1, 1, 3, 4, 6] # пример




origin_permutation = [1]
full_permutation = [1]
for i in range (2, len(vector) + 1):
    full_permutation.append(i)
    origin_permutation.append(i)

for i in range (len(vector) - 1, -1, -1):
    origin_permutation[i] = full_permutation[-vector[i] - 1]
    full_permutation.remove(full_permutation[-vector[i] - 1])

print (origin_permutation)

