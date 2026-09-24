class WeakPasswordError(Exception):
    pass
# Function to check password strength
def check_password(password):
    if password == "":
        raise ValueError("Password cannot be empty.")

    if len(password) < 8:
        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_+=<>?/"

    for char in password:
        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

    if not has_upper:
        raise WeakPasswordError(
            "Password must contain at least one uppercase letter."
        )

    if not has_lower:
        raise WeakPasswordError(
            "Password must contain at least one lowercase letter."
        )

    if not has_digit:
        raise WeakPasswordError(
            "Password must contain at least one digit."
        )

    if not has_special:
        raise WeakPasswordError(
            "Password must contain at least one special character."
        )

    return True


# Main function
def main():
    print("===================================")
    print("      PASSWORD STRENGTH CHECKER")
    print("===================================")

    while True:
        try:
            password = input(
                "Enter your password (or type 'exit' to quit): "
            )

            if password.lower() == "exit":
                print("Thank you for using Password Strength Checker!")
                break

            check_password(password)

            print("Password Strength: STRONG")
            print("Password meets all security requirements.")

        except ValueError as e:
            print("Error:", e)

        except WeakPasswordError as e:
            print("Weak Password:", e)

        except Exception as e:
            print("Unexpected Error:", e)


# Start program
if __name__ == "__main__":
    main()