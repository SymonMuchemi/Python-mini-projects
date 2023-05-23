import re

string = input("Enter a phone numer to validate:\nFormat: xxx-xxx-xxx-xxx: ")


def check_pattern(number):
    pattern = r'^\d{3}-\d{3}-\d{3}-\d{3}$' # Example 254 712 345 678
    result = re.match(pattern, number)

    if result:
        print("Validation successful")
    else:
        print("Format error!")


check_pattern(string)