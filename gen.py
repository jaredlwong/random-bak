import os, sys
import Image
from colorsys import hsv_to_rgb
from colorsys import hls_to_rgb
from random import random
from random import randint

def rgb_dtoi(rgb):
    rgb = list(rgb)
    rgb = map(lambda x: int(round(x*255)), rgb)
    rgb = map(lambda x: 255 if x > 255 else x, rgb)
    return tuple(rgb)

def rand_rgb_hsv(hue=None,sat=None,val=None):
    if hue == None: hue = randint(0,360)
    if sat == None: sat = randint(0,100)
    if val == None: val = randint(0,100)
    rgb = hsv_to_rgb(float(hue)/360.0,float(sat)/100.0,float(val)/100.0)
    return rgb_dtoi(rgb)

def rand_rgb_hls(hue=None,light=None,sat=None):
    if hue == None: hue = randint(0,360)
    if light == None: light = randint(0,100)
    if sat == None: sat = randint(0,100)
    rgb = hls_to_rgb(float(hue)/360.0,float(light)/100.0,float(sat)/100.0)
    return rgb_dtoi(rgb)


def rand_block(rgb_func, block_size):
    size = x, y = 500, 500
    im = Image.new('RGB', size)
    putpixel = im.im.putpixel

    for i in xrange(0,x,block_size):
        for j in xrange(0,y,block_size):
            endx = i+block_size
            endx = endx if endx < x else x
            rgb = rgb_func()
            for p in xrange(i,endx):
                endy = j+block_size
                endy = j+block_size if j+block_size < y else y
                for q in xrange(j,endy):
                    putpixel((p,q),rgb)

    im.save('random-bak.png')


teal_func = lambda: rand_rgb_hsv(randint(210,220),randint(16,20),randint(30,33))
gray_func = lambda: rand_rgb_hsv(0,0,randint(90,95))
bg_func = lambda: rand_rgb_hsv(214,randint(10,15),randint(30,35))
rand_block(bg_func, 10)


def rand_grid(reg_func, grid_func, block_size):
    size = x, y = 500, 500
    block = 9
    im = Image.new('RGB',size)
    putpixel = im.im.putpixel

    for i in xrange(x):
        for j in xrange(y):
            if i % block_size == 0 or j % block_size == 0:
                putpixel((i,j),grid_func())
            else:
                putpixel((i,j),reg_func())

    im.save('random-bak.png')

#rand_grid(gray_func,bg_func,9)
#bg_func_grid = lambda: rand_rgb_hsv(214,randint(5,10),randint(30,35))
#bg_func_reg = lambda: rand_rgb_hsv(214,randint(5,10),randint(30,35))
bg_func_grid = lambda: rand_rgb_hls(214,randint(20,25),randint(10,15))
bg_func_reg  = lambda: rand_rgb_hls(214,randint(30,35),randint(10,15))
#rand_grid(bg_func_reg,bg_func_grid,9)

def more_rand_grid(grid_func, block_size):
    size = x, y = 1439, 154
    im = Image.new('RGB',size)
    putpixel = im.im.putpixel

    for i in xrange(0,x,block_size):
        for j in xrange(0,y,block_size):
            start = randint(20,30)
            reg_func = lambda: rand_rgb_hls(214,randint(start,start+5),randint(10,15))
            for p in xrange(i,i+block_size):
                for q in xrange(j,j+block_size):
                    if p < x and q < y:
                        if p % block_size == 0 or q % block_size == 0:
                            putpixel((p,q),grid_func())
                        else:
                            putpixel((p,q),reg_func())

    im.save('random-bak.png')

more_rand_grid(bg_func_grid,9)


#    grid = lambda: rand_rgb_hsv(randint(210,220),randint(16,20),randint(26,29))
#    for i in xrange(0,x,block):
#        for j in xrange(0,y,block):
#            end = i+block
#            end = end if end < x else x
#            for p in xrange(i,end):
#                rgb = rand_rgb_hsv(randint(210,220),randint(16,20),randint(26,29))
#                putpixel((p,j),rgb)
#            end = j+block
#            end = end if end < y else y
#            for p in xrange(j,end):
#                rgb = rand_rgb_hsv(randint(210,220),randint(16,20),randint(26,29))
#                putpixel((i,p),rgb)
#            endx = i+block
#            endx = endx if endx < x else x
#            for p in xrange(i+1,endx):
#                endy = j+block
#                endy = j+block if j+block < y else y
#                for q in xrange(j+1,endy):
#                    rgb = rand_rgb_hsv(randint(210,220),randint(16,20),randint(30,33))
#                    putpixel((p,q),rgb)
#    #        rgb = rand_rgb_hls(0,randint(85,95),0)
#    #        rgb = rand_rgb_hsv(randint(230,240),randint(0,10),randint(90,100))
#    #        putpixel((i,j),rgb)

#    im.save('random-bak.png')
