class Character(object):
	name = ""
	job = ""
	race = ""
	exp = ""
	lvl = ""

	def __init__(self, name, job, race, exp, lvl)
		self.name = name
		self.job = job
		self.race = race
		self.exp = exp
		self.lvl = lvl
	
	def toString(self)
		print(self)
	
	def updateLevel(self)
		x = 0
		newlvl = 1
		expneeded = 0
		while x = false:	
			expneeded += (self.lvl -1 * 1000)
			newlvl += 1
			if exp >= expneeded:
				self.lvl = newlvl
				x = 1;

def createCharacter(name, job, race, exp, lvl)
	char = Character(name,job,race,exp,lvl)
	return char


