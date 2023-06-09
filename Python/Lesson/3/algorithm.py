# Алгоритмы
'''Алгоритмом называется набор инструкций для выполнения некоторой задачи. В
принципе, любой фрагмент программного кода можно назвать алгоритмом, но мы с
Вами рассмотрим 2 самых интересных алгоритмы сортировок:
● Быстрая сортировка
● Сортировка слиянием'''

# Быстрая сортировка
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))

# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
            
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
