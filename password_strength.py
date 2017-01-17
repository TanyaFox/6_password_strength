import re


def get_points_for_password_length(password):
    points = 0
    if len(password) <= 4:
        points += 0
    elif (len(password)) > 4 and (len(password) <=6):
        points += + 1
    elif len(password) > 6:
        points += + 2
    return points

def get_points_for_case_sensitivity(password):
    points = 0
    if not (password.isupper() or password.islower()):
        points = 2
    return points

def get_points_for_inclusion_of_numeric_digits(password):
    points = 0
    if re.search('\d', password):
        points = 2
    return points

def get_points_for_inclusion_of_special_characters(password):
    points = 0
    if re.search('\W', password):
        points = 2
    return points

def get_points_for_no_bthdays_and_phone_numbers(password):
    points = 0
    if not (re.search('\d[0-3]?\d-?\d[0-1]?\d-?[1]?[9]?\d\d', password)) and not (re.search('\+?\d{1}[0-9]{10}', password)):
        points = 2
    return points

def get_password_strength(password):
    score = 0
    score += get_points_for_password_length(password)
    score += get_points_for_case_sensitivity(password)
    score += get_points_for_inclusion_of_numeric_digits(password)
    score += get_points_for_inclusion_of_special_characters(password)
    score += get_points_for_no_bthdays_and_phone_numbers(password)
    return score


if __name__ == '__main__':
    password = input("Enter your password: ")
    password_strength = get_password_strength(password)
    print("Your password strength is ", password_strength)
