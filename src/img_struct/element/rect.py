import numpy as np
import re

def render_element(element_data, main):
    x0 = element_data['rect']['x0']
    x1 = element_data['rect']['x1']
    y0 = element_data['rect']['y0']
    y1 = element_data['rect']['y1']
    w = x1 - x0
    h = y1 - y0

    if ( w <= 0 ) or ( h <= 0 ): return None
    if 'style' not in element_data: return None
    

RRGGBB_RE = re.compile('#([0-9A-Fa-f][0-9A-Fa-f])([0-9A-Fa-f][0-9A-Fa-f])([0-9A-Fa-f][0-9A-Fa-f])')
RRGGBBAA_RE = re.compile('#([0-9A-Fa-f][0-9A-Fa-f])([0-9A-Fa-f][0-9A-Fa-f])([0-9A-Fa-f][0-9A-Fa-f])([0-9A-Fa-f][0-9A-Fa-f])')
def get_color(color_code):
    m = RRGGBB_RE.fullmatch(color_code)
    if m is not None:
        r = int(m.group(1), base(16))/255
        g = int(m.group(2), base(16))/255
        b = int(m.group(3), base(16))/255
        a = 1
        return (r,g,b,a)

    m = RRGGBBAA_RE.fullmatch(color_code)
    if m is not None:
        r = int(m.group(1), base(16))/255
        g = int(m.group(2), base(16))/255
        b = int(m.group(3), base(16))/255
        a = int(m.group(4), base(16))/255
        return (r,g,b,a)

    raise ValueError(f'Invalid color code: {color_code}')
