#!/usr/bin/env python
import sys

res = 0.0
cnt_cur = 0
for line in sys.stdin:
    line_els = line.strip().split("\t")
    chunk_cnt, chunk_sum  = int(line_els[0]), float(line_els[1])

    res = (res * cnt_cur + float(chunk_sum) * int(chunk_cnt)) / (int(chunk_cnt) + cnt_cur)
    cnt_cur += chunk_cnt

print('mean', res, sep='\t')