# Question 1: Controlled Multiplication loop
# Writing a program that multiplies consecutive integers starting from one until it becomes grater than the threshold.
# I am going to connect this to saving money and reaching a target of more than 100 dollars

target_savings_value = 100 # this is the threshold
current_savings_amount = 1 # this is the current product
integer_value_growth_rate_per_month = 1 # this is the multiplier

while current_savings_amount < target_savings_value:
    integer_value_growth_rate_per_month += 1
    current_savings_amount *= integer_value_growth_rate_per_month

print(f"The final savings amount (product) is {current_savings_amount}")
print(f"The integer that caused the product to exceed the target savings value (threshold) is {integer_value_growth_rate_per_month}")