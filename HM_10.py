# # Ex 1
# word = input("Enter")
#
# vowels = set("aeiou")
# set_word = set(word)
#
# print(set_word & vowels)

# # Ex 2
# set1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# set2 = {20, 14, ('Python', 'C', 12), 10, 11}
#
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set1 = set1.difference(set2)
# difference_set2 = set2.difference(set1)
# symmetric_difference_set = set1.symmetric_difference(set2)
#
# print("Union:", union_set)
# print("Intersections:", intersection_set)
# print("Difference:", difference_set1)
# print("Difference:", difference_set2)
# print("Symmetric:", symmetric_difference_set)

# # Ex 3
# set1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# set2 = {20, 14, ('Python', 'C', 12), 10, 11}
#
# if set1.issubset(set2):
#     print('set_1 is a subset of set_2')
# else:
#     elements = set2.difference(set1)
#     set1.update(elements)
# print(set1)


# Ex 4
tuple_1 = (11, "55", 54, "abc", 90, 102, "asdasd", "qwerty")

# Ex 7
list_1 = [12, 41, 5, 8, 0, 11, -7, 9, -1]
list_2 = [36, -12, 0, 18, -1, 12, 45, 21]

set_list_1 = set(list_1)
set_list_2 = set(list_2)

print(tuple(set_list_1 & set_list_2))

# # Ex 6
# list_1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, -6, 2, 8), 6, 2]
#
# x = 0
#
# for i in list_1:
#     for j in list_1[i]:
#         x += j
# print(x)

print('Hello World')

print('Welcome to my first Python')