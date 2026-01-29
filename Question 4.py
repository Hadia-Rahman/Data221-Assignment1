# Question 4: Sorted Search with conditions:
# writing a program that sorts the list and find all indices where the list value is greater than or equal to x
# print the first matching index if it exists
# using starter code for this question

from random import random
random_values = [random() for i in range(20)]
x = random()
sorted_list_of_random_values = sorted(random_values)
matching_indices_in_random_values = []
for index, random_value in enumerate(sorted_list_of_random_values):
    if random_value >= x:
        matching_indices_in_random_values.append(index)
print(f"The sorted list is {sorted_list_of_random_values}")
print(f"The value of x is {x}")
if matching_indices_in_random_values:
    print(f"The first matching index is {matching_indices_in_random_values[0]}")
else:
    print("Their is no matching index where the value is greater than or equal to x.")