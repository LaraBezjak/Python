import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import signal
import imageio
import os

path="./Gif"
if not os.path.exists(path):
  os.mkdir(path)
  print("Folder %s created!" % path)
else:
  print("Folder %s already exists" % path)
  
images = []

images = []

def simulate(numIter, A, B, f, k, dt, dA, dB, lapl, plot_iter):
    print("Running Simulation")
    start = time.time()

    for iter in range(numIter):
        A_new = A + (dA * signal.convolve2d(A, lapl, mode='same', boundary='fill', fillvalue=0) - (A * B * B) + (f * (1-A))) * dt
        B_new = B + (dB * signal.convolve2d(B, lapl, mode='same', boundary='fill', fillvalue=0) + (A * B * B) - (k * B)) * dt
        A = np.copy(A_new)
        B = np.copy(B_new)
        if (iter % plot_iter is 0):
            plt.clf()
            plt.imshow((B / (A+B)),cmap='Spectral')
            plt.axis('off')
            now = time.time()
            # print("Seconds since epoch =", now-start)
            # plt.show()
            filename = 'Gif/gs_'+str(iter)+'.png'
            plt.savefig(filename)
            images.append(imageio.imread(filename))

    return A, B

#GRID
grid_size = 101
numIter = 5000;
seed_size = 11
A = np.ones((grid_size,grid_size))
B = np.zeros((grid_size,grid_size))

# Seed the predators
B[int(grid_size/2)-int(seed_size/2):int(grid_size/2)+int(seed_size/2)+1, \
int(grid_size/2)-int(seed_size/2):int(grid_size/2)+int(seed_size/2)+1] = \
np.ones((seed_size,seed_size))

#VARIABLES
f = 0.055
k = 0.117
dt = 1.0
dA = 1.0
dB = 0.5
lapl = np.array([[0.05, 0.2, 0.05],[0.2, -1.0, 0.2],[0.05, 0.2, 0.05]])
plot_iter = 50


simulate(numIter, A, B, f, k, dt, dA, dB, lapl, plot_iter)
imageio.mimsave('Gif/gs_gif.gif', images)