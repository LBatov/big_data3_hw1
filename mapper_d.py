#!/usr/bin/env python
import sys
import string


res_mean = 0.0
res_disp = 0.0
cnt_cur = 0
for line in sys.stdin:
    cur_v = float(line.replace(',','.'))
    res_disp = (cnt_cur * res_disp + cur_v) / (1 + cnt_cur) + \
               cnt_cur * ((res_mean - cur_v) / (1 + cnt_cur)) ** 2 
    res_mean = (res_mean * cnt_cur + cur_v) / (1 + cnt_cur)
    cnt_cur += 1


print ('%s\t%s\t%s' % (cnt_cur, res_mean/cnt_cur, res_disp))