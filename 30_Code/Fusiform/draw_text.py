from PIL import Image, ImageDraw
from PIL import ImageFont
from .config import config

def measure_text(text):    
    font_size = config.FONT_SIZE
    font = ImageFont.truetype(config.DEFAULT_FONT_PATH, font_size)    
    # measure text    
    txtw, txth = font.getsize(text)
    return txtw, txth

def text2bitmap(text, im_dim):         
    font_size = config.FONT_SIZE
    font = ImageFont.truetype(config.DEFAULT_FONT_PATH, font_size)    

    # "L" for a 8bit bitmap    
    im = Image.new("L", im_dim)
    draw = ImageDraw.Draw(im)    
    draw.text((0,0), text, (255,), font=font)    
    return im