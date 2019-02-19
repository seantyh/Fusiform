from .split_text import split_text
from .draw_text import *
from .digest_image import Digestor
from .steps import *
from .spotlight import *

def aggregate_average(intext, digestor, **kwargs):
    frags = split_text(intext)
    N = 0
    Xsum = None
    _, txt0_h = measure_text(frags[0])
    for frag_x in frags:
        txt_w, _ = measure_text(frag_x)
        im_dim = (txt_w, txt0_h)
        im = text2bitmap(frag_x, im_dim)        
        X, n = digestor.digest(im, **kwargs)
        N += n
        
        if Xsum is None:
            Xsum = X
        else:
            Xsum += X
    avgX = (Xsum / N) / 255

    print(f"N: {N}, nChar: {sum([len(x) for x in frags])}")
    # transform avgX with logistic function, k is growth rate
    k = 5
    transX = (1 / (1 + np.exp(-k*(avgX - 0.5)))) * 255
    return transX