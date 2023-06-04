'''
Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''
data = "a a a b c a a d c d d"
resuit = []
for ind, val in enumerate(data):
    n=data[0:ind].count(val)
    resuit.append(f"{val}_{n}"if n>0 else val)
    # if n>0:
    #     resuit.append(f"{val}_{n}")
    # else:
    #     resuit.append(val)
print(" ".join(resuit))

input_string = "a a a b c a a d c d d"
amount_of_lettres = dict()
output_string = ""
for el in input_string:
    if el!=" ":
        if el not in amount_of_lettres:
            amount_of_lettres[el]=1
            output_string +=el
        else:
            output_string += el + "_"+str(amount_of_lettres[el])
            amount_of_lettres[el] +=1
    else:
        output_string = output_string + el
print(output_string)
#print(d)
