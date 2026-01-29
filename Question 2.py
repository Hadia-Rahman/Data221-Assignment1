# Question 2: Nested Dictionary from strings
# Writing a function that takes in a list of strings and returns a dictionary where the key in the key value pair is a string from the list
# and the value is the length of the string and weather it is even or odd.
# I am going to use a grocery list

def nested_dictionary_for_grocery_item_names(list_of_grocery_item_names):
    grocery_item_names_dictionary = {}
    for grocery_item_name in list_of_grocery_item_names:
        length_of_grocery_item_name = len(grocery_item_name)
        if  length_of_grocery_item_name % 2 == 0:
            length_of_grocery_item_name_parity = "even"
        else:
            length_of_grocery_item_name_parity = "odd"
        grocery_item_names_dictionary[grocery_item_name] = {
        "length": length_of_grocery_item_name,
        "parity": length_of_grocery_item_name_parity
    }
    return grocery_item_names_dictionary
print(nested_dictionary_for_grocery_item_names(["Salad", "Apple", "Banana"]))