from time import sleep

around = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

board = '''
_______________________
__#____________________
___#___________________
_###__________##_______
______________##_______
_______________________
_______________________
_________________#_____
_________________#_____
_________________#_____
_______________________
______________##_______
______________#________
_______________________
_______________________
_______________________
'''

def show(board):
	min_r = 99999999999999
	max_r = -99999999999999
	min_c = 99999999999999
	max_c = -99999999999999
	for i in board:
		min_r = min(min_r,i[0])
		min_c = min(min_c,i[1])
		max_r = max(max_r,i[0])
		max_c = max(max_c,i[1])
	for r in range(min_r,max_r+1):
		for c in range(min_c,max_c+1):
			if (r,c) in board:
				print("#",end="")
			else:
				print(" ",end="")
		print()
	print("---------------")

def parse(string):
	alive = set()
	for r, line in enumerate(string.split("\n")):
		for c, el in enumerate(line):
			if el == "#":
				alive.add((r,c))
	return alive

def potential(board):
	for cell in board:
		yield cell
		for i in around:
			yield (cell[0]+i[0],cell[1]+i[1])

def step(boardOld,boardNew,livefunc):
	alive = False
	for cell in potential(boardOld):
		neighbours = 0
		for i in around:
			if (cell[0]+i[0],cell[1]+i[1]) in boardOld:
				neighbours+=1
		old = cell in boardOld
		new = livefunc(old,neighbours)
		alive = alive or (not old and new)
		if new:
			boardNew.add(cell)
		elif cell in boardNew:
			boardNew.remove(cell)
	boardOld.clear()
	return alive

def conway(old, neighbours):
	if old:
		if neighbours > 3 or neighbours < 2:
			return False
	else:
		if neighbours == 3:
			return True
	return old

def main():
	board1 = parse(board)
	board2 = parse(board)
	show(board2)
	alive = True
	while alive:
		alive = step(board1,board2, conway)
		show(board2)
		board1,board2 = board2,board1
		sleep(0.1)

if __name__ == '__main__':
	main()


