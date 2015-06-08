'''
The Utils module describes certain functions that are useful, such as converting between coordinate systems.
'''


# Coordinate Utilities:
def algebraic_to_cartesian(algebraic):
	cartesian = [0,0]
	
	x_string = algebraic[:1]
	y_string = algebraic[1:]
	
	cartesian[0] = ord(x_string) - 96 - 1 # Subtract 96 so that an ASCII 'a' will come out as 1, 'b' will be 2, etc. subtract 1 for array
	cartesian[1] = int(y_string) - 1
	
	return cartesian
	
def cartesian_to_algebraic(cartesian):
	algebraic = str(chr(cartesian[0] + 97)) + str(cartesian[1] + 1)
	return algebraic
	
