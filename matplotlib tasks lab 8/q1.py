import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [12, 18, 22, 28, 35]

plt.plot(x, y1, color="pink", marker="o", label="y1")
plt.plot(x, y2, color="gray", marker="o", label="y2")

plt.title("two lines on one graph")
plt.xlabel("amazing x-axis")
plt.ylabel("incredible y-axis")
plt.legend(loc="lower right")

plt.show()
