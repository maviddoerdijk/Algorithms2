import numpy as np
x = np.zeros((5,5))
x += np.arange(5)
x2 = np.transpose(x)
print(x2)

print(x[0][1])