
# Задача: предложить улучшения кода для уже решённых задач:
# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# ___________________________44.________________________________
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# a = [int(input(f'Введи {i} координату точки а: ')) for i in 'xy']
# b = [int(input(f'Введи {i} координату точки а: ')) for i in 'xy']
# result = sum([(element[1] - element[0])**2 for element in zip(a,b)])**0.5
# print(result)


# ___________________________45.________________________________
#  Найти сумму чисел списка стоящих на нечетной позиции
# import random
# num_list =[random.randint(1,10) for i in range (6)]
# print(num_list)
# res = sum([value for indx, value in enumerate(num_list) if indx%2 == 1])
# print(res)

# ___________________________46.________________________________
#  Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

# import random
# num_list =[random.randint(1,10) for i in range (6)]
# print(num_list)
# res = [num_list[i]*num_list[-i-1] for i in range((len(num_list)//2)+len(num_list)%2)]
# print(res)

# ___________________________47.________________________________
# Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)
# n = int(input())

# res_list = [(-3)**i for i in range(n)]
# print(res_list)