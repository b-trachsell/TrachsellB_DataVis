import matplotlib.pyplot as plt

years = [1900,1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000]

pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4 ,4.8, 5.3, 5.7, 6.1]

# What is happening lmao
# 

plt.plot (years, pops, color=(255/255, 100/255, 100/255), linewidth= 6.0)

plt.ylabel("World population by billions")
plt.xlabel("Population growth by year")
plt.title("Global population growth 1900-2015", pad=20)

plt.show()