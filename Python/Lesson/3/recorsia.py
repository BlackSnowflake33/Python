# Рекурсия
#💡 Рекурсия — это функция, вызывающая сама себя.

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]
