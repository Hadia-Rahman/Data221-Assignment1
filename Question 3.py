# Question 3: Safe function Application
# Write a function that calculates the exponent of x to the y and if the y is negative don't append it to the list
# I will do this for a math question

def calculating_integer_base_value_to_a_positive_exponent(x,y):
    return x ** y

pairs_of_integers = [[5,2], [3,-1], [4,-2], [2,1], [1,0]]
resulting_list_of_computed_values = []
for x, y in pairs_of_integers:
    if y >= 0:
        resulting_list_of_computed_values.append(calculating_integer_base_value_to_a_positive_exponent(x,y))
    else:
        continue
print(resulting_list_of_computed_values)
