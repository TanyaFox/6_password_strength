import re


def get_password_strength(password):
    score = 0

    #get points for password length
    if len(password) <= 4:
        score += 0
    elif (len(password)) > 4 and (len(password) <=6):
        score += + 1
    elif len(password) > 6:
        score += + 2

    #get points for case sensitivity
    if not (password.isupper() or password.islower()):
        score += 2

    #get points for inclusion of numeric digits
    if re.search('\d', password):
        score += 2

    #get points for inclusion of special characters
    if re.search('\W', password):
        score += 2

    #get points for non inclusion dates of burth and phone numbers
    if not (re.search('\d[0-3]?\d-?\d[0-1]?\d-?[1]?[9]?\d\d', password)) and not (re.search('\+?\d{1}[0-9]{10}', password)):
        score += 2

    return score


if __name__ == '__main__':
    password = input("Enter your password: ")
    password_strength = get_password_strength(password)
    print("Your password strength is ", password_strength)
