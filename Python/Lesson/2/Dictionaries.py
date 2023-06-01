# Словари Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу. 
# В списках в качестве ключа используется индекс элемента. В словаре для определения элемента используется значение ключа (строка, число). 
dictionary = {} 
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
print(dictionary['left'])  # ← типы ключей могут отличаться 
print(dictionary['up'])   # ↑ типы ключей могут отличаться 
dictionary['left'] = '⇐' 
print(dictionary['left']) # ⇐ 
print(dictionary['type']) # KeyError: 'type' 
del dictionary['left'] # удаление элемента