#7.3   задача про три '2'


def combinate_3 (arg):
    result = []

    for i in range (0, arg.__len__() - 3):
        for j in range (1 + i, arg.__len__() - 2):
            for k in range (1 + j, arg.__len__()):
                temp = [arg[i] , arg[j], arg[k]]
                result.append(temp)


    return result


def permutate_3 (alph):
    result = []
    temp = ''
    for item in alph:
        temp = item
        for i in alph:
            temp+=i
            for j in alph:
                temp = item + i + j
                result.append(temp)
    return result



enumeration = [1,2,3,4,5,6]

alph = '1345678'

place_for_2 = combinate_3(enumeration)

for item in place_for_2: print (item)

res = permutate_3(alph)
# for item in res: print (item)

for places in place_for_2:
    for each in res:
        temp = each
        temp = temp[:places[0] - 1] + '2' + temp[places[0] - 1:]
        temp = temp[:places[1] - 1] + '2' + temp[places[1] - 1:]
        temp = temp[:places[2] - 1] + '2' + temp[places[2] - 1:]
        print (temp)

