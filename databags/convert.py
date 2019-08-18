#!/usr/bin/env python3

import os
import sys
import json

filename = 'uspechy.json'

def process_record(rec):
  directory = rec['id']
  rec_file = os.path.join(directory, 'contents.ls')
  
  if not os.path.isdir(directory):
    os.mkdir(directory)

  if os.path.isfile(rec['img']):
    os.rename(rec['img'], os.path.join(directory, rec['img']))

  with open(rec_file, 'w') as target_file:
    for item in ['title', 'priority', 'date', 'icon', 'img', 'img-attribution', 'link', 'description']:
      try:
        target_file.write(item)
        target_file.write(": ")
        if type(rec[item]) is list:  
          target_file.write(";".join(rec[item]))
        else:
          target_file.write(str(rec[item]))
        target_file.write('\n')

        if not item == 'description':
          target_file.write('---\n')
      except KeyError:
        continue

if not os.path.isfile(filename):
  print(filename, "not found")
  sys.exit()

with open(filename, "r") as read_file:
    data = json.load(read_file)

    for record in data['array']:
      process_record(record)