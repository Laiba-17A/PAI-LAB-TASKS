num = input("Please enter a 4-digit number: ")

d1 = int(num[0])
d2 = int(num[1])
d3 = int(num[2])
d4 = int(num[3])

d1, d4 = d4, d1
d2, d3 = d3, d2

d1 = (d1 + 7) % 10
d2 = (d2 + 7) % 10
d3 = (d3 + 7) % 10
d4 = (d4 + 7) % 10

encrypted = str(d1) + str(d2) + str(d3) + str(d4)
print(encrypted)