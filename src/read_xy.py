import numpy as np
import pylab as pl

# Read file
infile = open("../data/xy.dat","r")

# Initialise
x = []
y = []

# Read lines
for line in infile:
    x_, y_ = np.array(line.split(), dtype='float')
    x.append(x_)
    y.append(y_)

# Close file
infile.close()

# Convert to numpy array
x = np.array(x)
y = np.array(y)

# Plot and show
pl.plot(x,y)
pl.show()
