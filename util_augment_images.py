#!/usr/bin/python

# do run command "pip install Augmentor" first without quotes

import Augmentor
p = Augmentor.Pipeline("./data/test/")

p.rotate(probability=0.07, max_left_rotation=0.10, max_right_rotation=0.10)
p.zoom(probability=0.05, min_factor=0.11, max_factor=0.15)

p.sample(10000)