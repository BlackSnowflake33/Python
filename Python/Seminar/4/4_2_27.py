'''
Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним 
или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

Output: 13

'''
input_string ="She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
list_sring = input_string.upper().split()
list_sring_2 = input_string.split()
print(f"Без учета регистра: {len(set(list_sring))}")
print(f"Без учета регистра: {len(set(list_sring_2))}")

