#! /usr/bin/env python

import os
import argparse
import glob

argparser = argparse.ArgumentParser(description=None)
argparser.add_argument('-i','--input',required=True)
argparser.add_argument('-o','--output',required=True)
args = argparser.parse_args()

infilename = os.path.abspath(args.input)
output_dir = os.path.abspath(args.output)
if not os.path.exists(output_dir):
    os.makedirs(output_dir,mode=0755)

# generate count dict
counts = {}
sample = '.'.join(os.path.basename(infilename).split('.')[:-1])
with open(infilename,'r') as ip:
    for line in ip:
        ref_clone = line.split('\t')[2].strip()
        counts[ref_clone] = counts.get(ref_clone,0) + 1

# output counts
output_file = os.path.join(output_dir,"%s.csv" % sample)
with open(output_file,'w') as op:
    print >>op, '# ' + "ref_clone, " + sample  # header line
    for (ref_clone,ref_count) in counts.iteritems():
        record = [ref_clone,str(ref_count),str(ref_count)]
        print >>op, ','.join(record)
