from .config import config

def step_char_wise(im, **kwargs):    
    nchar = kwargs.get("nchar", 1)
    char_width = config.FONT_SIZE
    xoffset = round(kwargs.get("xoffset", 0) * char_width)
    step_size = char_width * nchar
    step_overlap = kwargs.get("step_overlap", False)
    if step_overlap:
        steps = list(range(xoffset, im.size[0], char_width))
    else:
        steps = list(range(xoffset, im.size[0], step_size))    
    return steps, step_size

