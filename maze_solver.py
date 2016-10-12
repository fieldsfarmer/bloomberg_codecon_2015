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




def main():
	r_c = '8  8'
	# r_c = input()
	r_c = r_c.split()
	r_c = list(map(int, r_c))
	row = r_c[0]
	col = r_c[1]

	maze = []
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

	# for l in sys.stdin:
	# 	maze.append(l.strip())

	# print(maze)
	# print(r_c)
	t = maze_solver(row,col,maze,(1,0),(row-2,col-1))
	for u in t:
		x,y = u
		print(x, end=",")
		print(y)

if __name__ == '__main__':
	main()