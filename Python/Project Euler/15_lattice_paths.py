# The path must be 40 long, 20 going down, 20 going right
# NOTE: We only have to generate half the paths, b/c symmetry
from random import randint

def findpaths(height,width):
	counter = 0
	extantpath = []
	tempcounter = 0
	while tempcounter < 40000:			#while there are still paths to be found, counter is a placeholder
		widthcounter = width
		heightcounter = height
		path = []
		pathexists = False
		for x in range(1, height + width + 1):

			# generate a path from constraints height and width WE NEED TO DO BETTER RANDOM NUMBERS MAKES THIS A PAIN!!!
			randnum = randint(1,2)
			if randnum == 1 and widthcounter > 0:
				widthcounter -= 1
				path.append(1)
			elif heightcounter > 0:
				heightcounter -= 1
				path.append(0)
		
		
		#check to see if path has already been generated, if not, increase counter and add to extantpaths
		for i in extantpath:
			if path == i:
				pathexists = True
				break
			else:
				pathexists = False

		if  pathexists == False and len(path) == width + height:
			extantpath.append(path)
			counter += 1
		tempcounter += 1

	return counter

print findpaths(6,6)
