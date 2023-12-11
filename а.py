

# def count_skuchnye_kvartiry(p, i):
#     count = 0
#     for m in range(p, i, 1): # step не обязательно, просто я уже к нему привык
#         m = str(m)
#         if m.count(m[0]) == len(m):
#             count += 1

# p = int(input("Введите количество квартир в доме: "))

# i = int(input("Введите номер квартиры в которой ответили"))

# result = count_skuchnye_kvartiry(p, i)

# print("Количество обзвоненных квартир: ", result)

import math
n = int(input())
a = int(input())
b = int(input())
time = 0
for i in range(n):
    time = max(time, a * i + 2 * (n-1-i) * b)

print(time)