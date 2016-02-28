#!/usr/bin/env python
# coding:utf-8

# ---------- imports -------------
import requests
import time 

# ---------- global vars ---------
gURL_btc_ticker="https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny"

# ---------- funcs ---------------
def myclock(func):
    start = time.clock()
    func()
    end = time.clock()
    print end, start, end - start
    return func

def mytime(func):
    start = time.time()
    func()
    end = time.time()
    print end - start

@mytime
def run_get():
    of = file("okcoin.log", "w")
    for i in xrange(50):
        lines = requests.get(gURL_btc_ticker).content
        of.write(lines+"\n")
    of.close()

# ---------- main ----------------
if __name__ == '__main__':
    import cProfile
    cProfile.run("run_get()", filename="ip.log")
    import pstats
    p = pstats.Stats("ip.log")
    p.sort_stats("time").print_stats()
