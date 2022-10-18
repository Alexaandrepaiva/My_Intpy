#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import numpy.random as rn
import sys
import benchmark_decorator as dectimer

if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]
@dectimer.bench_time(3, sys.argv[1], environment)
def compute_FFT(n):
    """
        Compute the FFT of an n-by-n matrix of data
    """
    matrix = rn.rand(n, n) + 1j * rn.randn(n, n)
    result = np.fft.fft2(matrix)
    result = np.abs(result)


n = int(sys.argv[1])

print('FFT: ', n)

compute_FFT(n)

print(' ')
