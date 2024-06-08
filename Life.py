from time import sleep

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
	print("\n".join(map(lambda x: "".join(x), board)).replace("_", " "))

def parse(string):
	arr = []
	width = 0
	for line in string.split("\n"):
		l = ["+"]
		if line == "":
			continue
		width = len(line)+2
		for el in line:
			l.append(el)
		l.append("+")
		arr.append(l)
	return [["+" for _ in range(width)]]+arr+[["+" for _ in range(width)]]

def step(boardOld,boardNew, livefunc):
	alive = False
	around = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
	for row in range(len(boardOld)):
		for col in range(len(boardOld[0])):
			if boardOld[row][col] == "+":
				continue
			neghbours = 0
			for a in around:
				if boardOld[row+a[0]][col+a[1]] == "#":
					neghbours += 1
			old = boardOld[row][col] == "#"
			new = livefunc(old, neghbours)
			alive = alive or (not old and new)
			boardNew[row][col] = "#" if new else "_"
	return alive

def conway(old, neghbours):
	if old:
		if neghbours > 3 or neghbours < 2:
			return False
	else:
		if neghbours == 3:
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

