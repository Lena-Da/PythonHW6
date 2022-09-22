# 6 - Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random
number=(random.randint(0,5))
print(number)
res_list=[(-3)**i for i in range(number)]
print(res_list)