#!/usr/bin/env python
import sys
import string
TRUE_MEAN = 152.75505277800508

cnt = 0
sum = 0
var = 0.0
for line in sys.stdin:
    cur_v = float(line.replace(',','.'))
    sum += cur_v
    cnt += 1
    var += (TRUE_MEAN - cur_v) ** 2


print ('%s\t%s\t%s' % (cnt, sum/cnt, var/cnt))