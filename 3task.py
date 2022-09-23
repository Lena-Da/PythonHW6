# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# import math
# point_a1=float(input("Введи координату точки A1: "))
# point_a2=float(input("Введи координату точки A2: "))
# point_b1=float(input("Введи координату точки B1: "))
# point_b2=float(input("Введи координату точки B2: "))
# solution=((point_b1-point_a1)**2)+((point_b2-point_a2)**2)
# result = (round(math.sqrt(solution),2))
# print("Расстояние между точками: ", result)

import math


point_str=input("Ввести через пробел две кординаты a, две кординаты b: ").split(" ")
point_list=list(map(int,point_str))
result=math.sqrt( ((point_list[0]-point_list[2])**2) + ((point_list[1]-point_list[3])**2))
print(result)

# Не поняла, куда добавить ограничение знаков после запятой?