import struct
import numpy as np
import random
from fpu.table_gen import table_gen_sqrt

NR_ITERATIONS = 1
#print("Newton-Raphson iterations: ", NR_ITERATIONS)

def as_float(a):
    return struct.unpack('<f', struct.pack('<l', np.int32(a)))[0]

def as_int(a):
    return np.uint32(np.uint32(struct.unpack('<l', struct.pack('<f', a))[0]))

#Generate table
table_sqrt = table_gen_sqrt() #Table containing coefficients
	
def fp32_invsqrt(a):
	a_int = as_int(a)
	a_sgn = a_int >> 31 #Must be 0 for sqrt calculation
	a_exp = (a_int >> 23) & 0xff #Exponent as int
	a_sfc_enc = a_int & 0x7fffff #Mantissa as int
	a_e0_value = (a_int | 0x3f800000) & 0x3fffffff # a with exponent 0 (1.Mantissa)
	a_e0_value = np.float32(as_float(a_e0_value)) # 1.Mantiassa for use in calculations

	#Find interval
	#group = (a_int >> 22) & 0x1 #2 intervals
	#group = (a_int >> 21) & 0x3 #4 intervals
	group = (a_int >> 20) & 0x7 #8 intervals
	#group = (a_int >> 19) & 0xf #16 intervals
	#group = (a_int >> 18) & 0x1f #32 intervals
	#group = (a_int >> 17) & 0x3f #64 intervals
	
	#Perform initial approximation
	approx = initial_approx(table_sqrt[group], a_e0_value)
	exp = a_exp - 127
	
	#Perform newton_raphson.
	iterations = 0
	while (iterations < NR_ITERATIONS):
		approx = newton_raphson(approx, a_e0_value)
		iterations = iterations + 1
		#print ("Iteration " + str(iterations) + " Approximated answer= " + str(approx))
		
	#Multiply with exponent
	if (np.mod(exp, 2) == 0):
		exp = -exp / 2
		final_approx = approx * np.float32(np.power(2, exp))
	elif (np.mod(exp, 2) == 1):
		exp = (exp - 1) / -2
		final_approx = (approx * np.float32(1/np.sqrt(2))) * np.float32(np.power(2,exp))
	
	#return final_approx
	return as_float(as_int(final_approx))
	
def initial_approx(table, value): #table = [a, b, c]
	ca = table[0]
	cb = table[1]
	cc = table[2]

	approx = np.float32(ca*value*value + cb*value + cc)
	return approx
	
	
def newton_raphson(approx, value):
	new_approx = np.float32((approx/2))*np.float32((3-(value*(approx*approx))))
	return new_approx
	