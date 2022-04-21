# This file contains all the functions needed for plotting the Julia and Mandelbrot sets.

# Importing necessary libraries
import numpy as np
from numba import vectorize
from matplotlib.colors import LogNorm
from matplotlib import cm
import matplotlib.pyplot as plt
import copy

# This is a vectorized implementation (via numba) of the escape-time algorithm (with threshold = 2). 
@vectorize
def stability(z, c, max_iter):
  z_i = z
  for i in range(max_iter):
    z_i = z_i**2 + c
    if abs(z_i) >= 2:
      return (i+1)/max_iter 
    else:
      i += 1 
  return 1.0

# This computes for the normalized escape counts for a grid of complex numbers.
def get_stability_map(c, max_iter = 100, pixel_density = 1):
    x = np.linspace(-1.5, 1.5, int(1000 * pixel_density))
    y = np.linspace(-1.25, 1.25, int(750 * pixel_density))
    z = x[np.newaxis, :] + y[:, np.newaxis] * 1j
    return np.flipud(stability(z, c, max_iter))

# This plots the Julia set of a given complex number c.
def plot_julia_set(c, max_iter = 500, pixel_density = 1.0, cmap = 'magma', banding = True, show_tick_marks = False):
  fig, ax = plt.subplots(figsize = (8, 6))
  stabilities = get_stability_map(c = c, max_iter = max_iter, pixel_density = pixel_density)
  if banding:
    # If banding is True, we use LogNorm to induce bands of colors in our plot. We also use set_bad to take care of masked values for LogNorm.
    my_cmap = copy.copy(cm.get_cmap(cmap)) 
    my_cmap.set_bad(eval(f'cm.{cmap}({1/max_iter})'))
    ax.imshow(stabilities, cmap = my_cmap, norm = LogNorm(), interpolation = None, aspect = 1.25/1.5)
  else:
    ax.imshow(stabilities, cmap = cmap, aspect = 1.25/1.5)
  if show_tick_marks:
    # If show_tick_marks is True, we make sure that the grid is adjusted properly to the size of the stabilities matrix. The ticks below are obtained through linear functions that perform grid adjustment.
    xtick_labels = np.linspace(-1.5, 1.5, 6)
    ax.set_xticks([(int(1000 * pixel_density) / 3) * (x + 1.5) for x in xtick_labels], labels = ['{:.1f}'.format(xtick) for xtick in xtick_labels])
    ytick_labels = np.linspace(-1.25, 1.25, 6)
    ax.set_yticks([-(int(750 * pixel_density) / 2.5) * (y - 1.25) for y in ytick_labels], labels = ['{:.1f}'.format(ytick) for ytick in ytick_labels])
  else:
    ax.set_xticks([])
    ax.set_yticks([])
  return fig

# This plots the Mandelbrot set and also labels a complex number c in the plot, allowing us to see whether it belongs to the Mandelbrot set or not.
def plot_mandelbrot_set(c, cmap = 'magma', banding = True, show_tick_marks = False):
  fig, ax = plt.subplots(figsize = (6, 6))
  ax.axis('equal')
  # Since there is only one Mandelbrot set, we no longer compute for it manually like what we did earlier with the Julia set. Instead, we compute the stability matrix beforehand and load it here.
  stabilities = np.load('mandelbrot_stabilities.npy')
  if banding:
    my_cmap = copy.copy(cm.get_cmap(cmap)) 
    my_cmap.set_bad(eval(f'cm.{cmap}({1/3000})'))
    ax.imshow(stabilities, cmap = my_cmap, norm = LogNorm(), interpolation = None, aspect = 1)
  else:
    ax.imshow(stabilities, cmap = cmap, aspect = 1)
  if show_tick_marks:
    xtick_labels = np.linspace(-2, 1, 6)
    ax.set_xticks([(1200 / 3) * (x + 2) for x in xtick_labels], labels = ['{:.1f}'.format(xtick) for xtick in xtick_labels])
    ytick_labels = np.linspace(-1.5, 1.5, 6)
    ax.set_yticks([-(1200 / 3) * (y - 1.5) for y in ytick_labels], labels = ['{:.1f}'.format(ytick) for ytick in ytick_labels])
  else:
    ax.set_xticks([])
    ax.set_yticks([])  
  ax.plot((1200 / 3) * (np.real(c) + 2), -(1200 / 3) * (np.imag(c) - 1.5), '.', markersize = 3)
  return fig

