
frontDet = 0

sample = [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]

for i in range (len(sample)):

	frontDet = frontDet << 1
	frontDet |= sample[i]
	print (str(sample[i])+ " "+ str(frontDet & 0x0003 ))
	#print (str(sample[i])+ " "+ str(frontDet))

