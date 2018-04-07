import numpy as np
import matplotlib.pyplot as plt

temp = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1])
ice_sale = np.array([215,325,185,332,406,522,412,614])

plt.plot(temp,ice_sale,"o")

p = np.polyfit(temp,ice_sale,1)
print(p)

plt.plot(temp,np.polyval(p,temp),"g-")
