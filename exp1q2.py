# 1. Array (List in Python)
my_array = [1, 2, 3, 4, 5]
my_array.append(6)  # Adding an element
print("Array:", my_array)
# 2. List
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")  # Removing an element
print("List:", my_list)
my_list.sort()  # Sorting the list
print("Sorted List:", my_list)
# 3. Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Tuple length:", len(my_tuple))
print("Count of 2 in tuple:", my_tuple.count(2))
# 4. Set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
print("Set:", my_set)
my_set.remove(3)  # Removing an element
print("Set after removal:", my_set)
# 5. Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict['age'] = 26  # Updating value for key 'age'
print("Dictionary:", my_dict)
print("Keys in dictionary:", my_dict.keys())
print("Values in dictionary:", my_dict.values())