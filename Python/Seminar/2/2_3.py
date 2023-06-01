'''
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась 
самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе. 
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50 
Input:    6 -> -20 30 -40 50 10 -10 
Output: 2
'''
num=int(input('Введите число N: '))
maxSeguence=0
currentSeguence=0
currentTemp=0
for i in range(num):
    currentTemp = int(input('Введите температуру: '))
    if currentTemp > 0:
        currentSeguence+=1
    else:
        if currentSeguence > maxSeguence:
            maxSeguence = currentSeguence
        currentSeguence = 0
    if currentSeguence > maxSeguence:
        maxSeguence = currentSeguence
print(maxSeguence)