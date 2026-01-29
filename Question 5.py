# Question 5: Circle Area Comparison with Validation
# Write a function that takes the radius from two circles, validates both radii are positive integers, and computes the area of each circle
# returns area of larger circles area that can be covered by smaller circles area
# invalid input needs a proper message
import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Invalid input radius must be a positive number."
    if not isinstance(radiusOfCircle1,int) or not isinstance(radiusOfCircle2,int):
        return "Invalid input radius must be an integer."
    area_of_circle1 =  math.pi * (radiusOfCircle1)**2
    area_of_circle2 =  math.pi * (radiusOfCircle2)**2
    if area_of_circle1 > area_of_circle2:
        bigger_area = area_of_circle1
        smaller_area = area_of_circle2
    elif area_of_circle1 < area_of_circle2:
        bigger_area = area_of_circle2
        smaller_area = area_of_circle1
    else:
        bigger_area = area_of_circle1
        smaller_area = area_of_circle2
    percentage_of_area_covered = (smaller_area/bigger_area) * 100
    return percentage_of_area_covered