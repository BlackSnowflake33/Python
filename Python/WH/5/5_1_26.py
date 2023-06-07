'''5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. 
Циклы использовать нельзя
Примеры/Тесты:
<function_name>(2,0) -> 1
<function_name>(2,1) -> 2
<function_name>(2,3) -> 8
<function_name>(2,4) -> 16
'''

def extent_num(num, exp_num):
    if (exp_num == 0):
        return 1
    if (exp_num != 0):
        return (num * extent_num(num, exp_num - 1))
num = int(input("Введите число: "))
exp_num = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", extent_num(num, exp_num))
