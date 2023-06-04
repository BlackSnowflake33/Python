# Функция — это фрагмент программы, используемый многократно

'''
Задание: Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

'''
# def sumNumbers(n):
# summa = 0
# for i in range(1, n + 1):
# summa += i
# print(summa)

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
        return 

n = int(input()) # 5
print(sumNumbers(n)) # 15