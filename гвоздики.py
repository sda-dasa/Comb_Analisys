#
# # задача про гвоздики
#
print ('w  r  p')

count = 15

for i in range (0, count, 2):
    for j in range (0, count, 2):
        if (i + j < count): print (i, j, 15 - i - j )
        else: break
