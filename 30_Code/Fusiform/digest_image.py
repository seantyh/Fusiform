import numpy as np
import matplotlib.pyplot as plt
from .config import config

class Digestor:
    def __init__(self, spotlight_func, step_func):
        self.spotlight_func = spotlight_func
        self.step_func = step_func

    def digest(self, im, **kwargs):
        xsteps, step_size = self.step_func(im, **kwargs)
        _, him = im.size

        X = np.zeros(shape=(him,step_size))
        for xo in xsteps:
            # Note np_im is a matrix, it follows the matrix (row, column) convention
            fim = self.spotlight_func(np.array(im), (0, xo, him, step_size))
            # plt.imshow(fim)
            # plt.show()
            X[:,:] += fim
        return X, len(xsteps)
    

class MatrixDigestor:
    def __init__(self, spotlight_func, step_func):
        self.spotlight_func = spotlight_func
        self.step_func = step_func

    def digest(self, im, **kwargs):
        xsteps, step_size = self.step_func(im, **kwargs)
        _, him = im.size
        nsteps = len(xsteps)

        Mr = him * step_size
        Mc = nsteps
        X = np.zeros(shape=(Mr, Mc))
        for col_i, xo in enumerate(xsteps):
            # Note np_im is a matrix, it follows the matrix (row, column) convention
            fim = self.spotlight_func(np.array(im), (0, xo, him, step_size))            
            fim_vec = np.reshape(fim, [-1,1]).flatten()          
            # plt.plot(fim_vec)
            # plt.show()
            X[:,col_i] = fim_vec
        return X, nsteps



