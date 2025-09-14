def is_valid_password(pwd):
    if len(pwd) < 8:
        return False

    l = False  # letter
    d = False  # digit
    s = False  # special
    special = "@#$%"

    for c in pwd:
        if c.isalpha():
            l = True
        elif c.isdigit():
            d = True
        elif c in special:
            s = True

    return l and d and s

p = input("Enter your password: ")

if is_valid_password(p):
    print("Valid password!")
else:
    print("Invalid password!")