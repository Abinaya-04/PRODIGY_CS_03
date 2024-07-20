import re

def password_complexity_checker(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one special character.")

    # Evaluate strength
    if strength <= 2:
        print("Password is weak.")
    elif strength <= 4:
        print("Password is medium.")
    else:
        print("Password is strong.")

    # Print feedback
    if feedback:
        print("Suggestions:")
        for suggestion in feedback:
            print(suggestion)

password = input("Enter a password: ")
password_complexity_checker(password)
