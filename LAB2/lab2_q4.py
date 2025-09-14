def closest_to_zero(tup):
    a = tup[0]
    b = tup[1]
    closest = a + b

    for i in range(len(tup)):
        for j in range(i + 1, len(tup)):
            s = tup[i] + tup[j]
            #if there is negative number in list thats why checking square
            if s * s < closest * closest:
                a = tup[i]
                b = tup[j]
                closest = s

    print("Pair with sum closest to zero:", a, "and", b)
    print("Their sum is:", closest)
    
numbers = (-10, -1, 2, 4, 8)
closest_to_zero(numbers)
