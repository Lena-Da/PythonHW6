# 5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import random
list_num=[random.randint(0,10) for i in range (5)]
print(list_num)
result=[list_num[i]*list_num[-1-i] for i in range (int(len(list_num)/2)+1)]
print(result)

