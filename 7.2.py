#задача 7.2


def combinate_2 (arg):
    result = []

    for i in range (0, arg.__len__() - 2):
        for j in range (1 + i, arg.__len__()):
            temp = [arg[i] , arg[j]]
            result.append(temp)

    return result




def combinate_3 (arg):
    result = []

    for i in range (0, arg.__len__() - 3):
        for j in range (1 + i, arg.__len__() - 2):
            for k in range (1 + j, arg.__len__()):
                temp = [arg[i] , arg[j], arg[k]]
                result.append(temp)

    return result


def permutate_2 (alph):
    result = []
    for i in alph:
        for j in alph:
            if i != j :
                temp = [i, j]
                result.append(temp)
    return result



enumerator = [1,2,3,4,5,6,7] # перечисление мест, в которые могут быть закинуты элементы


place_for_thrice = combinate_3(enumerator)# сочетания, определяющие номер мест которые занимает элемент, повторяющийся
# трижды

alphabet = [1,2,3,4,5,6,7,8]

reccured = permutate_2(alphabet) # массив всех пар повторяющихся элементов
i = 1
for recc in reccured:
    # убираем из алфавита те буквы, что мы выбрали сделать повторяющимися
    # if i == 1:
    #     print ('d')
    # else: i += 1
    new_alph = [alpha for alpha in alphabet]
    new_alph.remove(recc[0])
    new_alph.remove(recc[1])

    for places3 in place_for_thrice:
        # убираем из списка всех возможных позиций те позиции, которые мы выбрали для элемента, повторяющегося трижды
        new_enum = [enum for enum in enumerator]
        new_enum.remove(places3[0])
        new_enum.remove(places3[1])
        new_enum.remove(places3[2])
        places = combinate_2(new_enum) # все комбинации номеров мест, куда можно поставить элемент,
        # повторяющийся дважды

        for places2 in places:
            rest = GetPermutations(new_alph, 2) # все престановки без повторений для оставшихся (неповторяющихся) эл-тов

            for each in rest:
                temp = [r for r in each]
                temp.insert(places3[0] - 1, recc[0])
                temp.insert(places3[1] - 1, recc[0])
                temp.insert (places3[2] - 1, recc[0])
                temp.insert(places2[0] - 1, recc[1])
                temp.insert(places2[1] - 1, recc[1])

                print (temp)
