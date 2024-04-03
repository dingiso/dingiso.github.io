import os
import argparse
from filecmp import cmp

parser = argparse.ArgumentParser(description='This is compare script to compare nutstore markdown and posts')
parser.add_argument('nutdir', type=str, help=" the directory for nutstore")
args = parser.parse_args()

posts = [file for file in os.listdir('./_posts/')]
dif_mds = []
for root, dirs, files in os.walk(args.nutdir):
  dif_mds += [f for f in files if f[-3:] == '.md' and f in posts and not cmp(root+'/'+f,'./_posts/'+f)]
if len(dif_mds) > 0:
  print(f'Different Files: {dif_mds}')
