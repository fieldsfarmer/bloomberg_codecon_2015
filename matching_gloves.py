import collections

def matching_gloves(arr):
	d = collections.defaultdict(int)
	for a in arr:
		if isParlindrome(a):
			continue
		d[a]+=1
	res = 0
	for a in d.keys():
		t = a[::-1]
		if t in d and d[t]>0 and d[t] == d[a]:
			res += d[t]
			d[t] = 0
	if res == 0:
		for a in arr:
			if not isParlindrome(a):
				return -1
		return 0
	return res



def isParlindrome(a):
	t = a[::-1]
	return t == a

def main():
	# print(isParlindrome('ioi'))
	arr = ['bcd', 'erty', 'ytre', 'opipo', 'dcb']
	arr = ['abcde', 'edcba', 'abcde']
	arr = ['ioi', 'ertre', 'ghhg']
	print(matching_gloves(arr))

	# sz = int(input())
	# arr = []
	# for i in range(sz):
	# 	arr.append(input())
	# print(matching_gloves(arr))
	
if __name__ == '__main__':
	main()