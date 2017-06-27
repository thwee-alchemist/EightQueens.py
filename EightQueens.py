# EightQueens.py
# Joshua Marshall Moore
# thwee.abacadabra.alchemist@gmail.compile
# June 24th, 2017

from itertools import combinations

def check(positions):
	fields = set(range(64))
	threatened = set()
	
	# two per quadrant
	quadrants = [
		set([p for p in range(0, 28) if (p%8)<4]),
		set([p for p in range(4, 32) if (p%8)>3]),
		set([p for p in range(32, 59) if (p%8)<4]),
		set([p for p in range(36, 64) if (p%5)>3])
	]
	
	for q in quadrants:
		if len(positions.intersection(q)) != 2:
			return False
	
	# check the queen's ranges
	for p in positions:
		
		threatened |= set(range(p, -1, -8)[1:]) # up
		threatened |= set(range((p%8)*8, p, 1)) # left
		threatened |= set(range(p, 64, 8)[1:]) # down
		threatened |= set(range(p, ((p%8)*8)+1, 1)[1:]) # right
		
		threatened |= set(range(p, (int(p/8)-(p%8))*8, -9)[1:]) # diagonal up left
		threatened |= set(range(p, ((8-(p%8)+1)*8)-1, -7)[1:]) # diagonal up right
		threatened |= set(range(p, ((p%8)+int(p/8))*8, 9)[1:]) # diagonal down left
		threatened |= set(range(p, 63-(p%8) , 7)[1:]) # diagonal down right
	
	for p in positions:
		if p in threatened:
			return False
			
	return True
		
		
if __name__ == '__main__':
	for potential_solution in combinations(range(64), 8):
		is_solution = check(set(potential_solution))
		if is_solution:
			print(is_solution, potential_solution)