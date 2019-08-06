import os
import codecs
import linecache
import shutil

fd = 'KomatsuAnalyze'
inpath = 'C:/Users/zz17807/Documents/NetBeansProjects/'+fd+'/src'


total = 0
for root, dirs, files in os.walk(inpath):
    for f in files:
        with open(root+'/'+f, 'rb') as p:
            l = len(p.readlines())
            print(f+':'+str(l))
            total += l

print('Total:'+str(total))