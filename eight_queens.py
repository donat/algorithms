###############################################
# Solution for the eight queens problem       #
# Created by Donat Csikos <csdonat@gmail.com> #
# At 29/04/2012.                              #
###############################################

# The chessboard
class Board:
	def __init__(self):
		""" Fill the table with 0. If there is a queen, it will be replaced with a 1
		The table is addressed with two coordinates, ahich should be betweeen 0...7. """
		self._R8 = range(8)
		self._B = [[0,0,0,0,0,0,0,0] for i in self._R8]

	def put(self, x, y):
		""" Put a queen into the selected coordinate. """
		self._B[y][x] = 1

	def remove(self, x, y):
		""" Remove a queen from the selected coordinate. """
		self._B[y][x] = 0

	def print_table(self):
		""" Prints the current state of the table. """
		print "-------------------"
		for x in self._R8:
			print "|",
			for y in self._R8:
				print self._B[x][y],
			print "|"
		print "-------------------"

	def is_valid(self, x, y):
		""" Check if the selected position is valid for a new queen (no other queens 'see' it)."""
		for i in self._R8:
			# Check horizontal neighbours.
			if self._B[i][x] == 1:
				return False
			# Check vertical neighbours.
			elif self._B[y][i] == 1:
				return False
			else:	
				# Check diagonal neighbours.
				for xd, yd in [(x-i,y-i),(x-i,y+i),(x+i,y-i),(x+i,y+i)]:
					if xd in self._R8 and yd in self._R8:
						if self._B[yd][xd] == 1:
							return False
		# If no maches is found than return, that the field is available.
		return True
				
def eight_queen(b, x):
	""" Solver method. """
	# Print the state of the table.
	b.print_table()
	# If the function overaddresses the table, it means, that the previous steps have found a valid place. so thos
	# is the end of the algorithm and it should return true. 
	if x not in range(8):
		return True
	# Check for all the vertical possibilities.
	for y in range(8):
		if  b.is_valid(x, y):
			# If the current place is valid, put a queen there, and check whether there is a valid place on the next
			# column.
			b.put(x, y)
			chain = eight_queen(b, x + 1)
			# If no valid place for the next column, than remove the queen and try the row below this one.
			if not chain:
				b.remove(x,y)
				continue
			# Or else we are done, and return true.
			else:
				return True
	# If no places available in the passed column, than return false. 
	return False
					
# Start solving the algorithm.				
b = Board()
eight_queen(b,0)
