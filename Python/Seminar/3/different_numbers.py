'''Задача №17. Решение в группах 
Дан список чисел. Определите, сколько в нем встречается различных чисел. 
Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6'''

list_1=[1,1,2,0,-1,3,4,4]
emmply_list=[]

for i in list_1:
    if i not in emmply_list:
        emmply_list.append(i)
print(len(emmply_list))

lst1=[1,1,2,0,-1,3,4,4]
print(len(set(lst1)))
