'''
GitHub - SentinelByte
DanCohVax 2024
Enjoy coding
'''

import re

def is_valid_password(password):
    """
    Check if the password is valid.
    This function checks if the password is a non-empty string.
    Args:
        password (str): The password to validate.
    Returns:
        bool: True if the password is a valid non-empty string, False otherwise.
    """
    if not isinstance(password, str) or not password.strip():
        return False
    return True

def evaluate_password(password):
    """
    Evaluate the strength of the password and provide suggestions.
    This function checks if the password meets the strength requirements:
    - Minimum length of 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    Args:
        password (str): The password to evaluate.
    Returns:
        tuple: A string representing the strength ("Strong", "Moderate", or "Weak"),
        and a list of suggestions for improvement.
    """
    ## Define conditions for a strong password
    length = len(password) >= 8
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    ## Strength evaluation
    if all([length, has_upper, has_lower, has_digit, has_special]):
        return "STRONG!", []
    elif length and ((has_upper or has_lower) and (has_digit or has_special)):
        reasons = []
        if not has_upper:
            reasons.append("Missing an Uppercase letter")
        if not has_lower:
            reasons.append("Missing a Lowercase letter")
        if not has_digit:
            reasons.append("Missing a Digit")
        if not has_special:
            reasons.append("Missing a Special character. Ex: [ ! @ # $ % ^ & * ( ) ]")
        return "MODERATE", reasons
    else:
        reasons = []
        if not length:
            reasons.append("Too short (Must be at least 8 characters)")
        if not has_upper:
            reasons.append("Missing an Uppercase letter")
        if not has_lower:
            reasons.append("Missing a Lowercase letter")
        if not has_digit:
            reasons.append("Missing a Digit")
        if not has_special:
            reasons.append("Missing a Special character")
        return "WEAK", reasons

def main():
    """
    Main function for user interaction.
    This function allows the user to enter a password, evaluates its strength,
    and provides suggestions for improvement. The user can keep trying until
    they create a strong password or type 'exit' to quit.
    The function includes error handling for invalid passwords.
    """
    print("~~~~~~~~~~~~~~~~~~")
    print("Password Strength Checker\nEvaluate your password strength\nLet's begin")
    print("~~~~~~~~~~~~~~~~~~")

    while True:
        try:
            password = input("Enter a pass phrase (Or type 'exit' to quit): ").strip()
            if password.lower() == 'exit':
                print("Until the next time! Stay secure.")
                break
            
            if not is_valid_password(password):
                raise ValueError("Password cannot be empty or invalid.")

            strength, feedback = evaluate_password(password)
            print(f"\nPassword strength > {strength}")

            if feedback:
                print("Suggestions to improve pass phrase:")
                for reason in feedback:
                    print(f"  - {reason}")
            else:
                print("Congrats! You've created a strong pass phrase!")
                break

            print("\nTry again to improve your password!\n")
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

## Run the program
if __name__ == "__main__":
    main()
