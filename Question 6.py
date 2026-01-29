# Question 6: Distribution Analysis
# write a function that takes a list of numbers and returns a dictionary with each different number and the percentage of its appearance in the list
# I am going to connect this to temperature

def calculating_average_of_each_daily_temperature(daily_temperatures):
    total_number_of_daily_temperatures = len(daily_temperatures)
    average_of_each_daily_temperature = {}
    for unique_temperature in sorted(set(daily_temperatures)):
        number_of_times_each_unique_temperature_appears = 0
        for temperature in daily_temperatures:
            if temperature <= unique_temperature:
                number_of_times_each_unique_temperature_appears += 1
        percentage_of_unique_temperature = (number_of_times_each_unique_temperature_appears / total_number_of_daily_temperatures) * 100
        average_of_each_daily_temperature[unique_temperature] = percentage_of_unique_temperature
    return average_of_each_daily_temperature