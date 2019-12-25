casino_floor = str(input())

def verify(string):
	danger = bool(False)
	for i in string:
		if(not danger and (i == '$' or i == 'T')):
			danger = True
		elif(danger and (i == '$' or i == 'T')):
			return 'ALARM'
		elif(danger and i == 'G'):
			danger = False
	return 'quiet'
print(verify(casino_floor)) 
