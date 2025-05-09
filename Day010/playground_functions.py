def format_name(f_name, l_name):
    """
    Function to format a name in title case
    :param f_name, l_name: first name and last name
    :return: Concatenated values in Title case
    """
    return f_name.title() + " " + l_name.title()

print(format_name("KsleGHB", "wnkdaBBcsl"))


# Leap Year
# Write a program that returns True or False whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice
#
# This is how you work out whether if a particular year is a leap year.
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder
#
# e.g. The year 2000:
#     2000 ÷ 4 = 500 (Leap)
#     2000 ÷ 100 = 20 (Not Leap)
#     2000 ÷ 400 = 5 (Leap!)
#
# So the year 2000 is a leap year.
def is_leap_year(year):
    """
    Function to check if a given year is a leap year or not
    :param year: The year to check
    :return: True (year is a leap year) or False (if not)
    """

    div_by_4 = year % 4
    div_by_100 = year % 100
    div_by_400 = year % 400
    leap_year = False

    if div_by_4 == 0:
        if div_by_100 == 0:
            if div_by_400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True

    return leap_year


print(f"2000: {is_leap_year(2000)}")
print(f"2020: {is_leap_year(2020)}")
print(f"2024: {is_leap_year(2024)}")
print(f"2400: {is_leap_year(2400)}")
print(f"1700: {is_leap_year(1700)}")
print(f"1989: {is_leap_year(1989)}")
print(f"2100: {is_leap_year(2100)}")



