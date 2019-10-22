import collections
import math
"""
class Hexagon:

    def __init__(self, size):
        self.size = size 
        self.width = math.sqrt(3) * size
        self.height = 2 * size
        #height between adjacent hexagons is (height * 3/4)

    def function pointy_hex_corner(self, center, size, i):#i between 1 and 6 representing 6 points of a hexagon, returns x,y of vertice to be used to draw
        angle_deg = (60 * i) - 30
        angle_rad = math.pi / 180 * angle_deg
        return Point(center.x + size * math.cos(angle_rad), center.y + size * math.sin(angle_rad))
"""

class Hex:#int represtation of a hex
    def __init__(self, q, r, s): #qrs instead of xyz
    
        if (q + r + s != 0):
            return #q,r,s must equal 0

        self.q = int(q)
        self.r = int(r)
        self.s = int(s)
        

    def __eq__(self, a):
        return a.q == self.q and a.r == self.r and a.s == self.s

    def __ne__(self, a):
        return not(self == a)

    def get_coords(self):
        return (self.q,self.r,self.s)

class FractionalHex:#fractional represtation of a hex
    def __init__(self, q, r, s): #qrs instead of xyz
    
        if (q + r + s != 0):
            return #q,r,s must equal 0

        self.q = q
        self.r = r
        self.s = s

    def __eq__(self, a):
        return a.q == self.q and a.r == self.r and a.s == self.s

    def __ne__(self, a):
        return not(self == a)

    def get_coords(self):
        return (self.q,self.r,self.s)




hex_directions = [Hex(1,0,-1), Hex(1,-1,0), Hex(0,-1,1), Hex(-1,0,1), Hex(-1,1,0), Hex(0,1,-1)]

#return new hex with new coordinates, apply with self and other hex "a"
def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)
    
def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)

def hex_multiply(a, k):
    return Hex(a.q * k, a.r * k, a.s * k)

#distances
def hex_length(a):
    return int(abs(a.q) + abs(a.r) + abs(a.s) / 2)

def hex_distance(a, b):
    return hex_length(hex_subtract(a,b))

#neighbours
def hex_direction(direction): #direction 0-5
    return hex_directions[direction]

def hex_neighbour(a, direction):
    return hex_add(a, hex_direction(direction))


#layout
class Orientation:
    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, start_angle):
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3

        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

        self.start_angle = start_angle

layout_pointy = Orientation(math.sqrt(3.0), math.sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0, 
                            math.sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0,
                            0.5)

layout_flat = Orientation(3.0 / 2.0, 0.0, math.sqrt(3.0) / 2.0, math.sqrt(3.0), 
                            2.0 / 3.0, 0.0, -1.0 / 3.0, math.sqrt(3.0) / 3.0,
                            0.0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class Layout:
    def __init__(self, orientation, size, origin):#orientation, point, point
        self.orientation = orientation
        self.size = size
        self.origin = origin

def hex_to_pixel(layout, hex):
    orientation = layout.orientation
    x = (orientation.f0 * hex.q + orientation.f1 * hex.r) * layout.size.x
    y = (orientation.f2 * hex.q + orientation.f3 * hex.r) * layout.size.y
    return Point(x + layout.origin.x, y + layout.origin.y)

def pixel_to_hex(layout, point):
    orientation = layout.orientation
    pt = Point((point.x - layout.origin.x) / layout.size.x, (point.y - layout.origin.y) / layout.size.y)
    q = orientation.b0 * pt.x + orientation.b1 * pt.y
    r = orientation.b2 * pt.x + orientation.b3 * pt.y
    return FractionalHex(q, r, -q - r)

def hex_corner_offset(layout, corner):
    size = layout.size
    angle = 2.0 * math.pi * (layout.orientation.start_angle + corner) / 6
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))

def polygon_corners(layout, hex):
    corners = []
    center = hex_to_pixel(layout, hex)
    for i in range(0,6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))

    return corners

def hex_to_pixel_with_spacing(layout, hex, spacing):
    orientation = layout.orientation
    x = (orientation.f0 * hex.q  * spacing + orientation.f1 * hex.r  * spacing) * layout.size.x
    y = (orientation.f2 * hex.q  * spacing + orientation.f3 * hex.r  * spacing) * layout.size.y
    return Point(x + layout.origin.x, y + layout.origin.y)

def polygon_corners_with_spacing(layout, hex, spacing):
    corners = []
    center = hex_to_pixel_with_spacing(layout, hex, spacing)
    for i in range(0,6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))

    return corners

def hex_round(fractional_hex):
    q = int(round(fractional_hex.q, 0))
    r = int(round(fractional_hex.r, 0))
    s = int(round(fractional_hex.s, 0))
    q_diff = abs(q - fractional_hex.q)
    r_diff = abs(r - fractional_hex.r)
    s_diff = abs(s - fractional_hex.s)
    if (q_diff > r_diff and q_diff > s_diff):
        q = -r - s
    elif (r_diff > s_diff):
        r = -q - s
    else:
        s = -q - r
    
    return Hex(q, r, s)

#line drawing
def frange(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

def frange_le(start, stop, step=1):
    i = start
    while i <= stop:
        yield i
        i += step

def lerp(a, b, t):#float return
    return a * (1-t) + b * t

def hex_lerp(hex_a, hex_b, t):
    return FractionalHex(lerp(hex_a.q, hex_b.q, t), lerp(hex_a.r, hex_b.r, t), lerp(hex_a.s, hex_b.s, t))

def hex_line_draw(hex_a, hex_b):#hex hex, list of hex returned
    n = hex_distance(hex_a, hex_b)
    results = []
    step = 1.0 / max(n, 1)
    for i in frange_le(0,n):
        result.append(hex_round(hex_lerp(a, b, step * i)))

    return results


def hex_line_draw_nudge(hex_a, hex_b):#hex hex, list of hex returned, #nudge needed if bugging out when on edge
    n = hex_distance(hex_a, hex_b)
    a_nudge = FractionalHex(hex_a.q + 0.000001, hex_a.r + 0.000001, hex_a.s - 0.000002);
    b_nudge = FractionalHex(hex_b.q + 0.000001, hex_b.r + 0.000001, hex_b.s - 0.000002);
    results = []
    step = 1.0 / max(n, 1)
    for i in frange_le(0,n):
        result.append(hex_round(hex_lerp(a_nudge, b_nudge, step * i)))

    return results

#rotations
def hex_rotate_left(hex):
    return Hex(-hex.s, -hex.q, -hex.r)

def hex_rotate_left(hex):
    return Hex(-hex.r, -hex.s, -hex.q)


#map, {Hex, float}
"""
def create_map(map_radius):
    unordered_map = {}
    for q in frange_le(-map_radius, map_radius + 1):
        r1 = max(-map_radius, -q - map_radius)
        r2 = min(map_radius, -q + map_radius)

        for i in frange_le(r1, r2):
            unordered_map
"""
#offsets
OffsetCoord = collections.namedtuple("OffsetCoord", ["col", "row"])

EVEN = 1
ODD = -1
def qoffset_from_cube(offset, h):
    col = h.q
    row = h.r + (h.q + offset * (h.q & 1)) // 2
    return OffsetCoord(col, row)

def qoffset_to_cube(offset, h):
    q = h.col
    r = h.row - (h.col + offset * (h.col & 1)) // 2
    s = -q - r
    return Hex(q, r, s)

def roffset_from_cube(offset, h):
    col = h.q + (h.r + offset * (h.r & 1)) // 2
    row = h.r
    return OffsetCoord(col, row)

def roffset_to_cube(offset, h):
    q = h.col - (h.row + offset * (h.row & 1)) // 2
    r = h.row
    s = -q - r
    return Hex(q, r, s)