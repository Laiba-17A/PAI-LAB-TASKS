def top_3_countries(popdict):
    tempdict = popdict.copy()

    print("Top 3 most populated countries:")
    for _ in range(3):
        maxc = ""
        maxp = -1

        for country in tempdict:
            if tempdict[country] > maxp:
                maxp= tempdict[country]
                maxc = country

        print(maxc, "with population", maxp)
        del tempdict[maxc]

countries = {
    "China": 100000000,
    "India": 2000006000,
    "Afghanistan": 4567000,
    "Pakistan": 3000800000,
}

top_3_countries(countries)
