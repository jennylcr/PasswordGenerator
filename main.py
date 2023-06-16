# this program generates usernames based on student name and student id
# a password validation is also included while creating the account
def main():
    try:
        # get the first name from the user
        first_name = input("Please enter your first name: ").strip()
        # validate the first name
        valid_first_name = validate_name(first_name)
        # ask the user to try again until a correct name has entered
        while not valid_first_name:
            print("Invalid input. Please retry...")
            print()
            first_name = input("Please enter your first name: ").strip()
            valid_first_name = validate_name(first_name)

        # get the last name from the user
        last_name = input("Please enter your last name: ").strip()
        # validate the name
        valid_last_name = validate_name(last_name)
        # ask the user to try again until a correct name has entered
        while not valid_last_name:
            print("Invalid input. Please retry...")
            print()
            last_name = input("Please enter your last name: ").strip()
            valid_last_name = validate_name(last_name)

        # get the student id from the user
        student_id = input("Please enter your student ID: ").strip()
        # validate the student id
        valid_student_id = validate_student_id(student_id)
        # ask the user to try again until a correct student id has entered
        while not valid_student_id:
            print("Invalid input. Please retry...")
            print()
            student_id = input("Please enter your student ID: ").strip()
            valid_student_id = validate_student_id(student_id)

        # generate a login name for the user
        login_name = get_login_name(first_name, last_name, student_id)
        # return the login name to the user
        print("Your login name is " + login_name)

        # get the password from the user
        password = input("Please create a password: ").strip()

        # validate the password
        valid_password = validate_password(password)
        # ask the user to try again until a valid password has entered
        while password == "" or not valid_password[0]:
            print(valid_password[1])
            print("Please try again.")
            print()
            password = input("Please create a password: ").strip()
            valid_password = validate_password(password)
    except KeyboardInterrupt:
        print("Exit!")
    else:
        print("Password Created! Thank You!")


# this function validates first name and last name
def validate_name(name):
    # if the string is empty, return false
    if name == "":
        return False
    # if the string contains digits, return false
    elif name.isdigit():
        return False
    # if the string is less than 2 characters, return false
    elif len(name) < 2:
        return False
    # if the string is not all alphabetic letters, return false
    elif not name.isalpha():
        return False
    # otherwise, return true
    else:
        return True


# this function validates student id
def validate_student_id(student_id):
    # if the string is empty, return false
    if student_id == "":
        return False
    # if the student id is less than 5 characters or greater than 8 characters, return false
    elif len(student_id) > 8 or len(student_id) < 2:
        return False
    # if the string do not contain only alphabetic letters and digits, return false
    elif not student_id.isalnum():
        return False
    # if the string contains space, return false
    elif student_id.isspace():
        return False
    # otherwise, return true
    else:
        return True


# this function generates login name based on user input
def get_login_name(first_name, last_name, student_id):
    # get the first three characters of the student's first name
    part1 = first_name[0:3]
    # get the first three characters of the student's last name
    part2 = last_name[0:3]
    # get the last three characters of the student's ID number
    part3 = student_id[-3:]
    # Concatenate the three sets of characters to generate the user name
    return part1 + part2 + part3


# this function validates user password
def validate_password(password):
    # the result to return
    result = [False, ""]
    # set flags default value to false
    has_upper = False
    has_lower = False
    has_digit = False
    # check the password length
    if len(password) < 7:
        # set the error message
        result[1] = "Invalid password. A valid password must be at least seven characters in length."
    elif len(password) > 12:
        # set the error message
        result[1] = "Invalid password. A valid password must be no more than twelve characters in length."
    else:
        # check each character
        # if it meets the requirement, set the flag to true
        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
        # check flags, set the error message
        if not has_upper:
            result[1] = "Invalid password. A valid password must have at least one uppercase letter."
        elif not has_lower:
            result[1] = "Invalid password. A valid password must have at least one lowercase letter."
        elif not has_digit:
            result[1] = "Invalid password. A valid password must have at least one digit."
        else:
            result[0] = True
    return result


# call the main function
main()
