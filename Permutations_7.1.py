#задача 7.1

def GetPermutations(alphabet, k, new_configuration=None, used = None, count = 0):
    if used is None: # массив исключающий повторную генерацию одного и того же размещения
        used = [0] * len(alphabet)

    if len(new_configuration) == k:

        with open('permutations.txt', 'a') as file:
            file.write(', '.join(map(str, new_configuration)) + '\n')
        count+=1
        return count

    for i in range(len(alphabet)):
        if not used[i]:

            used[i] = True
            new_configuration.append(alphabet[i]) # формируем новое размещение - добавляем в него по элементу.

            count = GetPermutations(alphabet, k, new_configuration, used, count) # меняем порядок элементов в текущем размещении

            used[i] = False
            new_configuration.pop()

    return count
#
#

alphabet = [1, 2, 3, 4, 5, 6, 7, 8]
k = 5


with open('permutations.txt', 'w') as file:
    file.write('') # делаем файл пустым
    f = GetPermutations(alphabet, k, count = 0)

with open('permutations.txt', 'a') as file: file.write(f"{f}") # записываем в конец число полученных размещений

