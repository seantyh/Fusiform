import numpy as np
from .config import config

def digest_image(im, spotlight_func):    
    step_size = config.FONT_SIZE
    xsteps = list(range(0, im.size[0], step_size))
    wim, him = im.size
    
    X = np.zeros(shape=(him,64))
    for xo in xsteps:
        # Note np_im is a matrix, it follows the matrix (row, column) convention
        fim = spotlight_func(np.array(im), (0, xo, him, step_size), "rect")        
        X[:,:] += fim
    return X, len(xsteps)

    
