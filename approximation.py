
#Polynomial table
table = [[],[],[],[]]
table[0] = [float(-0.8), float(1.8)]
table[1] = [float(-0.5333), float(1.4667)]
table[2] = [float(-0.3809), float(1.2380)]
table[3] = [float(-0.2857), float(1.0714)]

#Collect input
value = float(input("Input: "))

#Place in correct group
group = 0

#Check input and do table lookup
def table_lookup(value):
	if float(1) <= value < float(1.25):
		group = 0
	elif float(1.25) <= value < float(1.5):
		group = 1
	elif float(1.5) <= value < float(1.75):
		group = 2
	elif float(1.75) <= value < float(2):
		group = 3
	else:
		print("Invalid value")
		value = float(input("Input: "))
	return group

answer = table[group][0]*value + table[group][1]
print("A=" + str(table[group][0]) + " B= " + str(table[group][1]))
print("Approximated answer = " + str(answer))
	
def main ():
		

