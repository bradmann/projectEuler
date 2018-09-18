before = {}
after = {}

if __name__ == '__main__':
	f = open('data/keylog.txt', 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		line = line.strip()
		before.setdefault(line[2], set([]))
		before[line[2]].add(line[0])
		before[line[2]].add(line[1])
		after.setdefault(line[0], set([]))
		after[line[0]].add(line[1])
		after[line[0]].add(line[2])
		before.setdefault(line[1], set([]))
		before[line[1]].add(line[0])
		after.setdefault(line[1], set([]))
		after[line[1]].add(line[2])
	print(before)
	print(after)