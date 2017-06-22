from random import randint
#dnd dice roll interpretter
#daniel dingess
#6-22-2017


#dice are input in [numdice]d[numsides]
#output is sum of [numdice] random numbers available on that dice


def evaluateRoll(formula):
	roll = 0;
	#split formula into parts
	explodedF = formula.split("+")
	#evaluate each segment
	for seg in explodedF:
		#just add constants
		if "d" not in seg:
			#print(seg)
			roll += int(seg)

		else:
			tempSum = 0
			atom = seg.split("d")
			#print(atom)
			if atom[0] is "1":
				tempSum += randint(1,int(atom[-1]))
			else:
				for x in range(0, int(atom[0])):
					tempSum += randint(1,int(atom[-1]))
			roll += tempSum
	
	return roll;
#test rolls
def main():
	print("2d20") 
	print(evaluateRoll("2d20"))
	print("3d100")
	print(evaluateRoll("3d100"))
	print("1d3")
	print(evaluateRoll("1d3"))
	print(evaluateRoll("2"))
	print("2d8+1d20+2")
	print(evaluateRoll("2d8+1d20+2"))
	
	

#call main			
if __name__ == "__main__":
    main()
