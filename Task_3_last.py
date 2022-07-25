'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''



from itertools import count


def Input_array(lenght):
    user_list = [i for i in range(lenght)]
    for i in range(lenght):
        print("Input number", i+1)
        user_list[i] = input()
    return user_list


def Get_ZeroPoint_numbers(arr, length):
    zero_point_list = [i for i in range(length)]
    for i in range(len(arr)):        
        count = 0
        for j in range(len(arr[i])):          
            # считаем кол-во элементов до точки, которые нужно заменить на ноль.
            if (arr[i])[j] != '.':
                count = count + 1
          
            if (arr[i])[j] == '.':
                break
        # если count меньше длины элемента начального списка, то значит число десятичное.
        if count != len(arr[i]):
            x = list(arr[i])
            for j in range(count):  # заменяем числа до точки нулями.
                x[j] = '0'         
            #zero_point_list[i] = float("".join(x))   
            zero_point_list[i] = "".join(x)  
        if count == len(arr[i]):
            #zero_point_list[i] = float(0)
            zero_point_list[i] = '0'
    return zero_point_list


def Delete_zero(arr):
    zero_deleted_list = [i for i in range(len(arr))]
    
    for i in range(len(arr)):
        count = -2 # Потому что не учитыввем первый 0 и "."
        for j in range(len(arr[i])):
            count +=1
        #(arr[i])[j] = (arr[i])[j]*10**count
        x = list(arr[i])
        y = float("".join(x)) 
        print(y)
        zero_deleted_list[i] = y*10**count
    return zero_deleted_list

print("Задайте размерность списка:")
list_length = int(input())

user_array = Input_array(list_length)
print(user_array)

zero_list = Get_ZeroPoint_numbers(user_array, list_length)
print(zero_list)

without_zero_list = Delete_zero(zero_list)
print(without_zero_list)
result = max(without_zero_list) - min(without_zero_list)

print("Разница между MAX и MIN дробной части:", result)


