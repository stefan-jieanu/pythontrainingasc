# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

def list_overlap(list1, list2):
    overlap = []
    for item in list1:
        if item in list2 and item not in overlap:
            overlap.append(item)
    return overlap

def list_overlap_using_sets(list1, list2):
    return list(set(list1) & set(list2))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
print(list_overlap(a, b))
print(list_overlap_using_sets(a, b))
