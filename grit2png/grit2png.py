#!/usr/bin/python3

'''
Created on 02/28/2020

@author: Joel Nauschütz
'''

# Todo: complete compression option

import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='Reduces tiles of PNG File')
parser.add_argument('input_file', help='Image File')
parser.add_argument('bitdepth', help='Bitdepth of Image')
parser.add_argument('width', type=int , help='Width of Image')
parser.add_argument('-gf', help='Grit File')
args = parser.parse_args()

gbagfx = '../tools/gbagfx/gbagfx'
grit = 'grit'
filename = os.path.basename(args.input_file).split(sep='.')[0]
twidth = args.width // 8
img_bin = filename + '.' + args.bitdepth
pal_bin = filename + '.gbapal'
map_bin = filename + '.bin'

if args.gf != None:
    subprocess.run([grit, args.input_file, '-ff', args.gf, '-m', '-ftb','-fh!' ])
else:
    subprocess.run([grit, args.input_file, '-m', '-ftb','-fh!' ])

os.rename(filename + '.img.bin', img_bin)
os.rename(filename + '.pal.bin', pal_bin)
os.rename(filename + '.map.bin', map_bin)
subprocess.run([gbagfx, img_bin, filename + '_r.png', '-palette',  pal_bin,
    '-width', str(twidth)])
subprocess.run([gbagfx, pal_bin, filename + '.pal'])
os.remove(img_bin)
os.remove(pal_bin)
