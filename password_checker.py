import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Minimum 8 characters required": length_error,
        "At least one uppercase letter required": uppercase_error,
        "At least one lowercase letter required": lowercase_error,
        "At least one digit required": digit_error,
        "At least one special character required": special_char_error
    }

    if all(not error for error in errors.values()):
        return "Strong Password ✅"
    else:
        return "Weak Password ❌\nIssues:\n" + "\n".join(f"- {rule}" for rule, error in errors.items() if error)

# Run the checker
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("\nPassword Feedback:\n" + result)
