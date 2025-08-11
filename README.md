Creating a list
my_list =[]

Appending items to the list
my_list.append(10)
my_list.append(20)    
my_list.append(30)
my_list.append(40)

Inserting nnew items/numbers at specified positions
my_list.insert(0, 15)

Extending the list with more items/numbers
my_list.extend([50, 60, 70])

Removing the last item/number
my_list.pop()

Sorting the list in ascending order
my_list.sort()

Finding the index of a specified number "30"
index_of_30 = my_list.index(30)
print(f"The index of '30' is: {index_of_30")

Printing the final state of the list
print("Final state oof the list:", my_list)

Run results:
The index of '30' is 3
Final state of my_list: [10, 15, 20, 30, 30, 50, 60]
