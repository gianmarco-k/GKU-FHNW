#Uebung 7
#Aufgabe 1

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)

farben = np.random.rand(1000, 3)

plt.scatter(x, y, c=farben, alpha=0.7)
plt.title("Übung 7, Aufgabe 1")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()



#Aufgabe 2

def f(x, y):
    return (np.exp(-x**2) * np.sin(y))

x = np.linspace(-3, 3, 300)
y = np.linspace(-np.pi, np.pi, 300)

plt.scatter(y, np.exp(-x**2) * np.sin(y))
plt.show()

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

plt.pcolormesh(X, Y, Z)
plt.title("Übung 7, Aufgabe 2")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()