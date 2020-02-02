import math

	# Code to convert hex to binary to list 
	

byte = 0x2C
data = []

#byte = 0b00011001
arr = []
for i in range(7, -1, -1):
	arr.append((byte & 1<<i)>>i)
print(arr)

