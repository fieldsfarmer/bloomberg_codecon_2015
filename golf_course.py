# following https://github.com/kdungs/codecon/blob/master/src/golf.cc
import sys

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

steps = None
data = sys.stdin.read().splitlines()
# print(data)
for line in data:
   steps = int(line)

# steps = 4

print(solution(1,9,steps))
