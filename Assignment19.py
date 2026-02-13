'''
Challenge: Implement the sorting algorithm without using any built-in sorting functions.



====================================

Description: Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order.
'''
def sort_list(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

list = [8, 2, 1, 3, 4]
sort_list(list)
print(list)