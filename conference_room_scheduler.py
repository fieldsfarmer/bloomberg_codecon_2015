import sys

class TimeRoom(object):
	def __init__(self,rooms):
		self.table = [[False]*(1+32) for _ in range(rooms+1)]
		self.total = rooms
	def book(self, room_id, time_slot, n):
		if room_id < 1 or room_id > self.total:
			return False
		if time_slot < 1 or time_slot > 32 or (time_slot+n-1)>32:
			return False
		res = False
		for i in range(time_slot, time_slot+n):
			if self.table[room_id][i]:
				return res
		res = True
		for i in range(time_slot, time_slot+n):
			self.table[room_id][i] = True
		return res

	def query(self, time_slot, n):
		res = []
		if time_slot < 1 or time_slot+n>32:
			return res
		for i in range(1,self.total+1):
			booked = False
			for j in range(time_slot, time_slot+n):
				if self.table[i][j]:
					booked = True
			if not booked:
				res.append(i)
		return res


# data = sys.stdin.read().splitlines()
# total = None
# res = []
# for line in data :
#     if not total:
#         total = int(line)
#     else:
#         res.append(line)
        
res = ['1-1-4', '1-2']
total = 3

tr = TimeRoom(total)

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
			output.append('None')
		else:
			output.append(t)

for r in output:
	if isinstance(r, list):
		for u in r:
			print(u, end=" ")
		print()
	else:
		print(r)