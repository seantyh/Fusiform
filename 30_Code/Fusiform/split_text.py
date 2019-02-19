import re

def split_text(text):
    zh_char_pat = r"[^\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]"
    frags = [x for x in re.split(zh_char_pat, text) if x]
    return frags