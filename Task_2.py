'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


def Input_array(lenght):
    user_array = [i for i in range(lenght)]
    for i in range(lenght):
        print("Input number", i+1)
        user_array[i] = int(input())
    return user_array


def Get_multiply(arr, length):
    if length % 2 == 0:
        iteration_amout = (length//2)
        result_array = [0 for k in range(length//2)]
    else:
        iteration_amout = (length//2) + 1
        result_array = [0 for i in range((length//2) + 1)]

    i = 0
    j = -1
    k = 0
    count = 0
    while count != iteration_amout:
        result_array[k] = arr[i]*arr[j]
        i = i + 1
        j = j + (- 1)
        k = k + 1
        count = count + 1
    return result_array


print("Задайте размерность списка:")
list_length = int(input())

user_array = Input_array(list_length)
print(user_array)

result = Get_multiply(user_array, list_length)
print(result)
