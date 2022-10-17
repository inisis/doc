> * title auto indent
```
plt.title('name of the title', wrap=True)
plt.tight_layout(pad=2, w_pad=3, h_pad=3)
```

> * plot step function
```
import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(-10, 10, 200)
x2 = np.linspace(-10, 10, 10)

y = np.exp(x1)
z = np.exp(x2)

plt.step(x1, y, color='r', label='exp 256 steps')
plt.step(x2, z, color='g', label='exp 10 steps')

plt.xlabel("Value")
plt.ylabel("X")
plt.title("Exp with different step sizes")

plt.legend()

plt.show()
```
