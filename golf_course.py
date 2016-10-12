

def solution(postion, target, steps):
	mp = [
		[4,6],
		[6,8],
		[7,9],
		[4,8],
		[0,3,9],
		[],
		[0,1,7],
		[2,6],
		[1,3],
		[2,4]
	]

	return helper(mp, postion, target, steps)

def helper(mp, postion, target, steps):
	res = 0
	if steps > 0:
		for i in mp[postion]:
			res += helper(mp, i, target, steps-1)
		return res
	if postion == target:
		return 1
	return 0



def main():
	steps = 4
	steps = 1
	# steps = int(input())
	# print(solution(1,9,steps))
	print(solution(1,6,steps))
if __name__ == '__main__':
	main()