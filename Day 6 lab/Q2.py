import re

def validate_password(password):
    # Regex pattern using lookahead assertions
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.match(pattern, password):
        print("Password is STRONG")
    else:
        print("Password is WEAK")
        print("Rules:")
        print("- Minimum 8 characters")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character (@$!%*?&)")

# Test password
pwd = input("Enter your password: ")
validate_password(pwd)



def demonstrate_modifiers():
    print("\n--- Regex Modifiers Demonstration ---")

    # IGNORECASE Example
    text1 = "Hello World"
    pattern1 = "hello"
    match1 = re.search(pattern1, text1, re.IGNORECASE)

    if match1:
        print("\nIGNORECASE Example:")
        print("Matched:", match1.group())

    # MULTILINE Example
    text2 = "Python\nJava\nC++"
    pattern2 = "^Java"
    match2 = re.search(pattern2, text2, re.MULTILINE)

    if match2:
        print("\nMULTILINE Example:")
        print("Matched:", match2.group())

    # DOTALL Example
    text3 = "Hello\nWorld"
    pattern3 = "Hello.World"
    match3 = re.search(pattern3, text3, re.DOTALL)

    if match3:
        print("\nDOTALL Example:")
        print("Matched:", match3.group())

demonstrate_modifiers()