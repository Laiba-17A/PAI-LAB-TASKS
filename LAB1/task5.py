name = input("Please enter your name: ")
year = int(input("Please enter your birth year: "))

first_three = name[:3]
password_name = first_three[0].upper() + first_three[1].upper() + first_three[2].lower()

last_two_digits = year % 100

ascii_val = ord(name[0].upper())
symbols = "@#%&*"
symbol_index = (ascii_val - 65) % 5
special_symbol = symbols[symbol_index]

password = password_name + str(last_two_digits).zfill(2) + special_symbol
print(password)