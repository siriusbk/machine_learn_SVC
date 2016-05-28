import matplotlib.pyplot as plt
from plt import style
style.use("ggplot")

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x,y)
plt.show()

