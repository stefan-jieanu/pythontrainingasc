# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

def list_overlap(list1, list2):
    return list(set(list1) & set(list2))


# Alternative 1: using a for loop
def list_overlap_loop(list1, list2):
    result = []
    for item in list1:
        if(item in list2 and item not in result):
            result.append(item)
    return result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("set intersection:", list_overlap(a, b))
print("for loop:        ", list_overlap_loop(a, b))