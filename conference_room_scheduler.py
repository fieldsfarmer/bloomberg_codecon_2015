import sys

class TimeRoom(object):
	def __init__(self,rooms):
		self.table = [[False]*(1+32) for _ in range(rooms+1)]
		self.total = rooms
	def book(self, room_id, time_slot, n):
		if room_id < 1 or room_id > self.total:
			return False
		if time_slot < 1 or time_slot > 32 or (time_slot+n)>32:
			return False
		res = False
		for i in range(time_slot, time_slot+n+1):
			if self.table[room_id][i]:
				return res
		res = True
		for i in range(time_slot, time_slot+n+1):
			self.table[room_id][i] = True
		return res

	def query(self, time_slot, n):
		res = []
		if time_slot < 1 or time_slot+n>32:
			return res
		for i in range(1,self.total+1):
			booked = False
			for j in range(time_slot, time_slot+n+1):
				if self.table[i][j]:
					booked = True
			if not booked:
				res.append(i)
		return res



def main():
	res = []
	res = ['1-1-4', '1-2']
	# total_rooms = int(input())
	total_rooms = 3

	# for l in sys.stdin:
	# 	res.append(l.strip())

	tr = TimeRoom(total_rooms)

	output = []
	for q in res:
		arr = q.split('-')
		arr = list(map(int, arr))
		# print(arr)
		if len(arr) == 3:
			if tr.book(*arr):
				output.append('Y')
			else:
				output.append('N')
		elif len(arr) == 2:
			t = tr.query(*arr)
			if not t:
				output.append('')
			else:
				output.append(t)
	for r in output:
		if isinstance(r, list):
			for i in r:
				print(i, end=" ")
		else:
			print(r)


	# for i in range(time_slot, time_slot+n+1):
	# line = sys.stdin.readline().strip()
	# while line:
	# 	res.append(int(line))
	# 	line = sys.stdin.readline().strip()
	# print(res)
if __name__ == '__main__':
	main()