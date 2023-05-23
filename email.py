import re

string = input("Enter a email address to validate:  ")


def check_pattern(number):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    result = re.match(pattern, number)

    if result:
        print("Validation successful")
    else:
        print("Format error!")


check_pattern(string)