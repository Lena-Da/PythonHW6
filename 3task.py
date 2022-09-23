# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math


point_str=input("Ввести через пробел две кординаты a, две кординаты b: ").split(" ")
point_list=list(map(int,point_str))
result=math.sqrt( ((point_list[0]-point_list[2])**2) + ((point_list[1]-point_list[3])**2))
print(result)

# Не поняла, куда добавить ограничение знаков после запятой?