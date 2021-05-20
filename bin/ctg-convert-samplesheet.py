#!/usr/bin/env python
# coding: utf-8
# import libs
import pandas as pd
import sys

orig = sys.argv[1]
nf = sys.argv[2]

print ("Using samplesheet    : %s" % orig)
print ("Parsing to new sheet : %s" % nf)

origsheet = pd.read_csv(orig,header=0,skiprows=1)
newsheet = origsheet[['Sample_ID','index']]
newsheet.insert(0,'Lane',0)
newsheet.to_csv(nf,header=None,index=False)

