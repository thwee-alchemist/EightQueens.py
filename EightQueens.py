# EightQueens.py
# Joshua Marshall Moore
# thwee.abacadabra.alchemist@gmail.com
# June 24th, 2017

# The eight queens problem consists of setting up eight queens on a chess board
# so that no two queens threaten each other. 

# This is an attempt to find all possible solutions to the problem. 

# The board is represented as a set of 64 numbers each representing a position 
# on the board. Array indexing begins with zero. 

# 00 01 02 03 04 05 06 07
# 08 09 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31
# 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47
# 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63

# Test:
# The following combination should yield a True from the check function.

# 6, 9, 21, 26, 32, 43, 55, 60

from itertools import combinations
import pdb

def check(positions):

	fields = set(range(64))
	threatened = set()
	
	# two queens per quadrant
	quadrants = [
		set([p for p in range(0, 28) if (p%8)<4]),
		set([p for p in range(4, 32) if (p%8)>3]),
		set([p for p in range(32, 59) if (p%8)<4]),
		set([p for p in range(36, 64) if (p%8)>3])
	]
	
	#for q in quadrants:
	#	if len(positions.intersection(q)) != 2:
	#		return False
			
	# check the queen's ranges
	for pos in positions:
	
		threatened |= set(range(pos, -1, -8)[1:]) # up
		threatened |= set(range(pos, 64, 8)[1:]) # down
		threatened |= set(range(pos, int(pos/8)*8-1, -1)[1:]) # left
		threatened |= set(range(pos, (int(pos/8)+1)*8, 1)[1:]) # right

		# down right diagonal:
		# There are two conditions here, one, the position is above the
		# diagonal, two, the position is below the diagonal.
		# Above the diagonal can be expressed as pos%8>int(pos/8).
		# In the event of a position above the diagonal, I need to limit the 
		# range to 64-(pos%8) to prevent warping the board into a field that 
		# connects diagonals like Risk. 
		# Otherwise, 64 suffices as the ending condition. 
		threatened |= set(range(pos, 64-(pos%8) if ((pos%8)<=int(pos/8)) else 64, 9)[1:]) # down right
		
		# up left diagonal:
		# Similarly, if the position is above the diagonal, -1 will suffice as 
		# the range's ending condition. Things are more complicated if the
		# position is below the diagonal, as I must prevent warping, again. 
		threatened |= set(range(pos, ((int(pos/8)-(pos%8))*8)-1 if ((pos%8)<=int(pos/8)) else -1, -9)[1:]) # up left
		
		# up right diagonal:
		# Above the diagonal takes on a different meaning here, seeing how I'm
		# dealing with the other diagonal. It is defined by pos. Now I
		# restrict the range to a (pos%8)*8, creating a boundary along the right
		# side of the board. 
		threatened |= set(range(pos, (pos%8)*8 if (pos%8)>=(pos%7) else -1, -7)[1:]) # up right
		
		# down left diagonal:
		# I reuse the same definition of the diagonal as above.
		threatened |= set(range(pos, ((pos%8)+1)*8 if (pos%8)>=(pos%7) else 64, 7)[1:]) # down left
	
	pdb.set_trace()
	
	if len(positions.intersection(threatened)) > 0:
		return False
	
	return True
		
		
if __name__ == '__main__':

	# print(check(set([55]))) # pass
	# print(check(set([62]))) # pass
	# print(check(set([63]))) # pass
	# print(check(set([48]))) # pass
	# print(check(set([57]))) # pass
	# print(check(set([56]))) # pass
	# print(check(set([8])))  # pass
	
	print(check(set([1])))  # fail
	print(check(set([0])))
	print(check(set([6])))
	print(check(set([15])))
	print(check(set([7])))


	print(
		check(set([6, 9, 21, 26, 32, 43, 55, 60]))
	)

	# for potential_solution in combinations(range(64), 8):
		# is_solution = check(set(potential_solution))
		# if is_solution:
			# print(is_solution, potential_solution)
