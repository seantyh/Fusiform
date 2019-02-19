import numpy as np

def spotlight(img, rect, shape, **kwarg):
    if shape == "gaussian":
        filtered = spotlight_gaussian(img, rect, shape, **kwarg)
    else:
        filtered = spotlight_rectangle(img, rect, shape, **kwarg)
    
    return filtered

def get_filtered_shape(img, coord):
    w, h = img.shape
    x, y, sw, sh = coord 
    
    if x > w or y > h:
        raise ValueError(f"{(x, y)} not in img dim {(w, h)}")
    if x + sw > w:
        sw = w - x
        
    if y + sh > h:
        sh = h - y
    
    return x, y, sw, sh

def spotlight_gaussian(img, coord, shape, **kwarg):
    return None

def spotlight_rectangle(img, coord, shape, **kwarg):
    x, y, sw, sh = get_filtered_shape(img, coord)
    padw = 0; padh = 0
    if sw < coord[2]:
        padw = coord[2] - sw
    if sh < coord[3]:
        padh = coord[3] - sh
    
    simg = img[x:(x+sw), y:(y+sh)]
    fimg = np.pad(simg, ((0, padw), (0, padh)), "constant")
    
    return fimg

