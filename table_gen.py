import struct
import numpy as np

INTERVALS = 16
interval_len = 1/INTERVALS
print(INTERVALS)

def as_int(a):
    return np.uint32(np.uint32(struct.unpack('<l', struct.pack('<f', a))[0]))

def table_gen_sqrt():	
	table_sqrt = []

	#Calculate coefficients for each interval using Gregory Forward algorithm
	for i in range(0, INTERVALS):
		xi = 1 + (i * interval_len)
		xip1 = xi + interval_len
		xm = (xip1+xi)/2
		
		k = xm - xi
		
		yi = 1/np.sqrt(xi)
		yip1 = 1/np.sqrt(xip1)
		ym = 1/np.sqrt(xm)
		
		a_interm = yip1 - 2*ym + yi
		b_interm = yip1 - yi
		
		k2 = 2*k
		ksq2 = 2*k*k
		ksq = k * k
		
		xmsq = xm * xm
		
		a = np.float32(a_interm / ksq2)
		b = np.float32((b_interm / k2) - ((xm * a_interm) / (ksq)))
		c = np.float32(((xmsq * a_interm) / ksq2) - ((xm * b_interm) / k2) + ym)
		
		table_sqrt.append([a, b, c])	
	
	return table_sqrt

