my_set = {1, 2, 3, "Hello", 3.24, 1, 2, False} #Dulplicated values will be removed in set
print(type(my_set)) #Data type of my_set is set
print(my_set) #note:the order may vary (not in order).
#my_set[0] = "Start" This will come error because sets are unordered and do not support indexing. Additionally, set are immutable

my_set.add("World")
print(my_set)

my_second_set = {3, 4, 5}
union_set = my_set.union(my_second_set)
print(union_set)

intersection_set = my_set.intersection(my_second_set)
print(intersection_set)

difference_set = my_set.difference(my_second_set)
print(difference_set)

my_set.clear()
print(my_set)