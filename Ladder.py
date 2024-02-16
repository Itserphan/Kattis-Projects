from math import *

h, v = map(int, input().split())


if 1 <= h <= 10000 and 1 <= v <= 89:
    print(ceil(h / sin(radians(v))))