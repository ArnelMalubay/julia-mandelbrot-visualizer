# This file simply generates the normalized escape counts of the grid (x,y) where x ranges from -2 to 1 and y from -1.5 to 1.5 with respect to the Mandelbrot set. This allows us to just load the computed values later on.

# Importing necessary libraries
import numpy as np
from numba import vectorize

# This is a vectorized implementation (via numba) of the escape-time algorithm (with threshold = 2). 
@vectorize
def get_mandelbrot_stability(c, max_iter):
  z_i = 0
  for i in range(max_iter):
    z_i = z_i**2 + c
    if abs(z_i) >= 2:
      return (i+1)/max_iter 
    else:
      i += 1 
  return 1.0

# We then used the function above on the grid defined below and save the results to an npy file.
x = np.linspace(-2, 1, 1200)
y = np.linspace(-1.5, 1.5, 1200)
z = x[np.newaxis, :] + y[:, np.newaxis] * 1j
mandelbrot_stabilities = np.flipud(get_mandelbrot_stability(z, 3000))
np.save('mandelbrot_stabilities', mandelbrot_stabilities)