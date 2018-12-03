#!/usr/bin/env/python

import sys
import numpy as np
import map_draw as md

#first argument - generated map size
size = int(sys.argv[1])

class GenMap:
    def __init__(self, map_size):
        self.m_s = map_size

        #generate two-dimensional array randomly filled with zeros and ones
        self.map_array = np.random.randint(2, size = (map_size, map_size))


if (size > 100):
    print("Map size too big, using maximum allowed value (10000 fields)")
    size = 100

gen_map = GenMap(size)
md.show_map(gen_map)
