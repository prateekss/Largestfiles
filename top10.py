#!/usr/bin/env python
import sys
import optparse
import subprocess

parser=optparse.OptionParser()
parser.add_option('-p','--path',dest='path',help='path of the directory')
(opt,args)=parser.parse_args()

if opt.path is None:
   #enter file path
   #format may change according to os.
   opt.path = input('Enter path:')
cmd1='find %s -not -type d -exec ls -sh  {} \;|sort -rh|head -n 10' % opt.path # this cmd is for linux os.
proc=subprocess.call(cmd1,shell=True)

