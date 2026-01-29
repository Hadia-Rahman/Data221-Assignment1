# Question 7: Time Conversion Function
# write a function that converts an inputted number of seconds from midnight in to the format Hours minutes seconds AM/PM
# if input is invalid a message should be returned.

def convert_seconds_to_time(secondsfrommidnight):
    # validating user input
    if secondsfrommidnight < 0:
        return "The number of seconds from midnight cannot be negative."
    elif secondsfrommidnight >= 86400:
        return "The number of seconds from midnight cannot be greater than 86399."
    elif not isinstance(secondsfrommidnight, int):
        return "The number of seconds from midnight must be an integer."
    # conversions
    hours_in_the_24hour_clock = secondsfrommidnight // 3600
    remaining_seconds_after_hour_conversion = secondsfrommidnight % 3600
    minutes = remaining_seconds_after_hour_conversion // 60
    seconds = remaining_seconds_after_hour_conversion % 60

    if hours_in_the_24hour_clock < 12:
        period = "AM"
    else:
        period = "PM"

    #Making hours from 24hour clock to the 12hour clock
    hours = hours_in_the_24hour_clock % 12
    if hours == 0:
        hours = 12

    return f"{hours} {minutes} {seconds} {period}"

