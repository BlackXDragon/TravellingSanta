# %%
import numpy as np
import matplotlib.pyplot as plt
print("Imports done")

# %%
x = [1]
y = [1]

fig = plt.figure()
ax = fig.add_subplot(111)

fig.show()
fig.canvas.draw()

for i in range(0,100):
    ax.clear()
    ax.plot(x,y)
    x.append(x[-1]+1)
    y.append(y[-1]*2)
    fig.canvas.draw()

# %%
x = [1]
y = [1]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

fig.show()
fig.canvas.draw()

for i in range(0,100):
    ax.clear()
    ax.plot(x,y)
    x.append(x[-1]+1)
    y.append(y[-1]*2)
    fig.canvas.draw()


