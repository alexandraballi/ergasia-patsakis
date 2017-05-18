print "pliktrologise apo poio sistima se poio thes na metatrapei o arithmos \n"
print "apo dekadiko se duadiko grapse <<decbin>> \n"
print "apo duadiko se dekadiko grapse <<bindec>> \n"
print "apo duadiko se dekaeksadiko grapse <<binex>> \n"
print "apo dekaeksadiko se duadiko grapse <<exbin>> \n"
userinput=raw_input("poio apo ta 4 thes ? \n")
arithmos=raw_input("dwse ton arithmo \n")
#arithmos=int(arithmos)
if userinput=="bindec":
	result=int(arithmos,2)
	print "to apotelesma einai %d" %result
if userinput=="decbin":
	arithmos=int(arithmos)
	x=arithmos
	k=[]
	while (arithmos>0):
		a=int(float(arithmos%2))
		k.append(a)
		arithmos=(arithmos-a)/2
	k.append(0)
	string=""
	for j in k[::-1]:
		string=string+str(j)
	print('to apotelesmagia %d einai %s'%(x, string))
if userinput=="binex":
	result=hex(int(arithmos,2))
	print "to apotelesma einai %s" %result
if userinput=="exbin":
	value = arithmos
	b = bin(int(value, 16))
	b[2:]
	b[2:].zfill(32)
	print "to apotelesma einai %s" %b

	
	
