
def sort(stdlist):
    n = len(stdlist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if stdlist[j][1] < stdlist[j + 1][1]:
                # Swap the tuples
                temp = stdlist[j]
                stdlist[j] = stdlist[j + 1]
                stdlist[j + 1] = temp
    return stdlist
def top_std(stdlist):
    sort(stdlist)
    print("Top 3 students:")
    i = 0
    while i < 3 and i < len(stdlist):
        student = stdlist[i]
        name = student[0]
        marks = student[1]
        print(i + 1, ".", name, "-", marks, "marks")
        i = i + 1

students = [
    ("Laiba", 85),
    ("Arshia", 92),
    ("Hania", 78),
    ("Zara", 95),
    ("Fatima", 88)
]

top_std(students)
