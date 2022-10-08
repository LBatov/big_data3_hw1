#!/usr/bin/env python
import sys
import string

cnt = 0
sum = 0
for line in sys.stdin:
    sum += float(line.replace(',','.'))
    cnt += 1

print ('%s\t%s' % (cnt, sum/cnt))