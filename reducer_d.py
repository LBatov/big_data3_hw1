#!/usr/bin/env python
import sys

res_mean = 0.0
res_disp = 0.0
cnt_cur = 0
for line in sys.stdin:
    line_els = line.strip().split("\t")
    chunk_cnt, chunk_sum, chunk_var  = int(line_els[0]), float(line_els[1]), float(line_els[2])

    
    res_disp = (cnt_cur * res_disp + chunk_cnt * chunk_var) / (chunk_cnt + cnt_cur) + \
               cnt_cur * chunk_cnt * ((res_mean - chunk_sum) / (chunk_cnt + cnt_cur)) ** 2 
    res_mean = (res_mean * cnt_cur + chunk_sum * chunk_cnt) / (chunk_cnt + cnt_cur)
    cnt_cur += chunk_cnt

print('disp', res_disp, sep='\t')