# 2 - Найти сумму чисел списка стоящих на нечетной позиции

import random
list_num=[random.randint(0,10) for i in range (6)]
print(list_num)
list_res=[list_num[i] for i in range(len(list_num)) if i%2 != 0]
print(sum(list_res))

