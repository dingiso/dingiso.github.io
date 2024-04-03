import os
import argparse
from filecmp import cmp

parser = argparse.ArgumentParser(description='This is compare script to compare nutstore markdown and posts')
parser.add_argument('nutdir', type=str, help=" the directory for nutstore")
args = parser.parse_args()

# 11 to delete the date and time
posts = [file for file in os.listdir('./_posts/')]
names = [file[11:] for file in posts]
dif_mds = []

for root, dirs, files in os.walk(args.nutdir):
  for f in files:
    if f[-3:] != '.md':
      continue
    try:
      idx = names.index(f)
      if not cmp(root+'/'+f,'./_posts/'+posts[idx]):
        dif_mds.append(posts[idx])
    except ValueError:
      continue

if len(dif_mds) > 0:
  print(f'Different Files: {dif_mds}')
