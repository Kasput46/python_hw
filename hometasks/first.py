import matplotlib.pyplot as plt
import numpy as np
import torch as t

figure, axis = plt.subplots(2,2)
x = np.array([1, 2, 3, 4, 5])

axis[0,0].plot(x,x**2, color="red")
axis[0,1].plot(x,x**3)

plt.show()