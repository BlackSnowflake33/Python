'''
Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем 
(число 0 не входит в последовательность)”. 
Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше 
ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

Примечание: Программные коды на следующих слайдах
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)

'''

num = int(input("Введите число N:"))
list_1 = []
for i in range(num+1):
    list_1.append(3*i+1)
print(list_1)

num_1 = int(input("Введите число N:"))
lst = [0]*(3*num_1+2)
for i in range(num_1+1):
    x = 3*i + 1
    lst[x]=x

print(lst)



num = int(input("Введите число N:"))
list_2 = []
for i in range(num+1):
    list_2.append(0)
    list_2.append(3*i+1)
    list_2.append(0)
list_2.pop()
print(list_2)
