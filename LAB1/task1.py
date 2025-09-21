num = int(input("Please enter a number: "))

float_num = float(num)
string_num = str(num) 
complex_num = complex(num)

# Print each type conversion and its type
print(f"Original number (int): {num}, Type: {type(num)}")
print(f"Float version: {float_num}, Type: {type(float_num)}")
print(f"String version: '{string_num}', Type: {type(string_num)}")
print(f"Complex version: {complex_num}, Type: {type(complex_num)}")

temp = abs(num)
while temp > 1:
    temp = temp - 2

is_divisible = temp == 0

print(f"Is {num} divisible by 2? {is_divisible}")