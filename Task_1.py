'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''


def Input_array(lenght):
    user_array = [i for i in range(lenght)]
    for i in range(lenght):
        print("Input number", i+1)
        user_array[i] = int(input())
    return user_array


def Get_summ(arr):
    sum = 0
    for i in range(len(arr)):
        if i % 2 != 0:
            sum = sum + arr[i]
        else:
            sum = sum
    return sum


print("Задайте размерность списка:")
list_length = int(input())

user_array = Input_array(list_length)
print(user_array)

result = Get_summ(user_array)
print(result)
