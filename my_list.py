# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting value 15 at the second position
my_list.insert(1, 15)

# Extending the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting the list in ascending order
my_list.sort()

# Finding the index of the value 30
index_of_30 = my_list.index(30)

# Printing the list and the index of 30
print("Modified List:", my_list)
print("Index of 30:", index_of_30)
