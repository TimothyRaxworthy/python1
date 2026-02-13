'''
Challenge: Optimize the function to handle large input lists efficiently.

==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.
'''

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2)) #check if there are similar between the lists

#two lists
list1 = [12,2323,4,5,67]
list2 = [12,4,67]

#print result
print(find_common_elements(list1, list2))