'''
Challenge: Ensure that the function works correctly with tuples of different lengths.



=============================================

Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.
'''


def concat_tuples(list1, list2):
    return list1 + list2

list1 = (1,2,3,4,5,6, "yes")
list2 = (1,2,3,4,5,14,1412,235)

print(concat_tuples(list1, list2))
