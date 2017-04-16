#! /usr/local/bin/python

import subprocess
from pprint import pprint

dir_struct = subprocess.check_output(['find', '.'])

dir_struct_lines = dir_struct.split('\n')

#print dir_struct_lines
dir_struct_map = {}
dir_struct_map['0.'] = []
dir_struct_lines = dir_struct_lines[:-1]

for dir_struct_line in dir_struct_lines[1:]:
  fnames = dir_struct_line.split('/')
  #print "Processing " + dir_struct_line
  for i in range(1,len(fnames)):
    curr = str(i) + fnames[i]
    parent = str(i - 1) + fnames[i - 1]
    parent_clist = dir_struct_map[parent]
    if curr not in parent_clist:
      parent_clist.append(curr)
      dir_struct_map[parent] = parent_clist
      dir_struct_map[curr] = []
    #print parent + '==>' + str(dir_struct_map[parent])

dir_struct_map = {k : v for k,v in dir_struct_map.iteritems() if v}

#pprint(dir_struct_map)

def print_dir_struct(padding, d, k):
  if k not in d:
    return
  for e in d[k]:
    #plen = len(padding)
    #pcnt = plen / 2
    #t1 = ''
    #for i in range(pcnt):
    #  t1 = (i * ' ') + '|'
    #t1 += (padding + '|')
    #print t1
    print (padding + '|')
    print(padding + '|_' + e[1:])
    print_dir_struct(padding + '  ', d, e)

print('.')
print_dir_struct('', dir_struct_map, '0.')
print('\n')

