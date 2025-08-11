my_list =[]
# This file defines a list named my_list
# that can be used to store items.
# You can append items to this list using my_list.append(item)

my_list.append(10)
my_list.append(20)    
my_list.append(30)
my_list.append(40)

my_list.insert(0, 15)# Inserting 15 at the second position in the list.

my_list.extend([50, 60, 70])  # Extending the list with numbers 50, 60, and 70

my_list.pop()  # This will remove the last item from the list
# The last item (70) is removed from the list

my_list.sort() # Sorting the list in ascending order
# The list is now sorted in ascending order

index_of_30 = my_list.index(30)  # Finding the index of the item "30"
# This will return the index of "30" in the sorted list
print(f"The index of '30' is: {index_of_30}")

# Printing the final state of the list
print("Final state of my_list:", my_list)