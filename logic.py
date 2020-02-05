from code import*
from const import*

out_buf  = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0]

string = [0] * 8
count = 0

for i in range (len(out_buf)):

	string.insert(8, out_buf[i])
	string.pop(0)
	if string in array2C:
		print ("Got it! " + str(count) + " times from " +str(i))
	count +=1
