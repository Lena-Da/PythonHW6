# 1 - Определить, присутствует ли в заданном списке строк, некоторое число

list_elem=["2","h1ello","world","2","!"]
result=list(filter(lambda x: "1" in x, list_elem))
print(result)
# Выводит ['h1ello']