#Problem        : Finals Spring 2015 - Maze Solver
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def maze_solver(row, col, maze, start, end):
	path = [start]
	v = [[False]*col for _ in range(row)]
	helper(row,col,maze,start,end,path,v)
	return path

def helper(row, col, maze, start, end, path, v):
	if start == end:
		return True
	x, y = start
	for i,j in (0,1),(1,0),(-1,0),(0,-1):
		a = x+i
		b = y+j
		if 0<=a<row and 0<=b<col and maze[a][b] == '_' and not v[a][b]:
			v[a][b] = True
			path.append((a,b))
			if helper(row,col,maze,(a,b),end,path,v):
				return True
			else:
				v[a][b] = False
				path.pop()
	return False


# data = sys.stdin.read().splitlines()
# r_c = ''
# maze = []
# for line in data :
#     if not r_c:
#        r_c = line list(map(int, line.split()))
#     else:
#         maze.append(line)

r_c = '8  8'
maze = [
	'XXXXXXXX',
	'____X__X',
	'XX_XX_XX',
	'XX_____X', 
	'XXXX_XXX', 
	'X_____XX', 
	'X_XXX___', 
	'XXXXXXXX'
]

r_c = list(map(int, r_c.split()))
row = r_c[0]
col = r_c[1]

t = maze_solver(row,col,maze,(1,0),(row-2,col-1))
for u in t:
	x,y = u
	print(x, end=",")
	print(y)
