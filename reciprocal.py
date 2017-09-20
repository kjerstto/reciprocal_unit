
#Polynomial table for f(x)=1/x and f(x)=sqrt(x)
table = [[],[],[],[]]
table[0] = [float(-0.8), float(1.8), float(-0.4222), float(1.4222)]
table[1] = [float(-0.5333), float(1.4667), float(-0.3117), float(1.2840)]
table[2] = [float(-0.3809), float(1.2380), float(-0.2422), float(1.1799)]
table[3] = [float(-0.2857), float(1.0714), float(-0.1952), float(1.0976)]

def receive_input(): #Recieve input x
	valid_input = False
	while (valid_input == False):
		value = float(input("Input: "))
		if float(1) <= value < float(2):
			valid_input = True
		else:
			valid_input = False
			print ("Invalid value!")
	return value
	
def compare (value):
	group = 0
	if float(1) <= value < float(1.25):
		group = 0
	elif float(1.25) <= value < float(1.5):
		group = 1
	elif float(1.5) <= value < float(1.75):
		group = 2
	elif float(1.75) <= value < float(2):
		group = 3
	return group

def initial_approx(a, b, value):
	approx = a*value + b
	print("A=" + str(a) + " B= " + str(b))
	print("Approximated answer = " + str(approx))
	return approx

def newton_raphson(approx, value, operation):
	if operation == 1:
		new_approx = approx*(2-(approx*value))
	else:
		new_approx = (approx/2)*(3-(value*(approx*approx)))
	return new_approx
	
def main():
	#Select operation. 1 for reciprocal, 2 for invserse square root. 
	operation = input("Reciprocal(1)/Sqrt(2)? ")
	value = receive_input()
	group = compare(value)
	if operation == 1:
		approx = initial_approx(table[group][0], table[group][1], value)
	else: 
		approx = initial_approx(table[group][2], table[group][3], value)
	iterations = 0
	while(iterations < 4):
		approx = newton_raphson(approx, value, operation)
		iterations = iterations + 1
		print ("Iteration " + str(iterations) + " Approximated answer= " + str(approx))
	if operation == 2:
		approx = approx*value
	print("Final approximation= " + str(approx))
	
main()	
	
	
	