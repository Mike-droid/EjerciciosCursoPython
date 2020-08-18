# list and dictionary comprehensions

# new_list = [expression(i) for i in old_list if filter(i)]

#Example of list: 
values = [2, 4, 6, 8, 10]
doubled_values = [x*2 for x in values]
print(doubled_values) # Outputs [4, 8, 12, 16, 20]

#Example of dictionary
squares = {num: num**2 for num in range(1,11)}
print(squares)