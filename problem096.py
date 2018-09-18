def box_range(x, y):
	rangex = []
	rangey = []
	if 0 <= x <= 2:
		rangex = [0, 1, 2]
	elif 3 <= x <= 5:
		rangex = [3, 4, 5]
	else:
		rangex = [6, 7, 8]
	if 0 <= y <= 2:
		rangey = [0, 1, 2]
	elif 3 <= y <= 5:
		rangey = [3, 4, 5]
	else:
		rangey = [6, 7, 8]
	return {'x': rangex, 'y': rangey}


def box_cant_be(board, x, y):
	ranges = box_range(x, y)
	cants = []
	for i in ranges['y']:
		for j in ranges['x']:
			if i == y and j == x:
				continue
			if board[i][j] != 0:
				cants.append(board[i][j])
	return cants

def row_cant_be(board, x, y):
	cants = []
	for i in range(9):
		if board[y][i] != 0 and i != x:
			cants.append(board[y][i])
	return cants

def col_cant_be(board, x, y):
	cants = []
	for i in range(9):
		if board[i][x] != 0 and i != y:
			cants.append(board[i][x])
	return cants

def cant_be(board, x, y):
	cants = []
	cants.extend(box_cant_be(board, x, y))
	cants.extend(row_cant_be(board, x, y))
	cants.extend(col_cant_be(board, x, y))
	return list(set(cants))

def solved(board):
	for row in board:
		rowcount = 0
		for item in row:
			rowcount += item
			if item == 0:
				return False
		if rowcount != 45:
			return False
	return True

def guesses(board):
	guessboard = [list(row) for row in board]
	guesses = 0
	for x in range(9):
		for y in range(9):
			if board[y][x] != 0:
				continue
			cants = cant_be(board, x, y)
			possibles = list(set([1,2,3,4,5,6,7,8,9]).difference(cants))
			guessboard[y][x] = possibles
			guesses += len(possibles)
	return guesses, guessboard

def best_guess(board):
	guess = None
	best = 9
	for x in range(9):
		for y in range(9):
			if board[y][x] != 0:
				continue
			cants = cant_be(board, x, y)
			possibles = list(set([1,2,3,4,5,6,7,8,9]).difference(cants))
			if len(possibles) < best:
				guess = {'x': x, 'y': y, 'possibles': possibles}
				best = len(possibles)
	return guess

def copyboard(board):
	return [list(row) for row in board]

def solve(board):
	updated = True
	while updated == True and solved(board) == False:
		updated = False
		for x in range(9):
			for y in range(9):
				if board[y][x] != 0:
					continue
				cants = cant_be(board, x, y)
				if len(cants) == 8:
					answer = list(set([1,2,3,4,5,6,7,8,9]).difference(cants))[0]
					board[y][x] = answer
					updated = True
	return solved(board)

def guess_and_solve(board):
	guess = best_guess(board)
	x = guess['x']
	y = guess['y']
	possibles = guess['possibles']
	for possible in possibles:
		newboard = copyboard(board)
		newboard[y][x] = possible
		is_solved = solve(newboard)
		if is_solved:
			return True, newboard
		else:
			is_solved, newboard2 = guess_and_solve(newboard)
			if is_solved:
				return True, newboard2
	return False, None

if __name__ == '__main__':
	f = open('data/sudoku.txt')
	lines = f.readlines()
	sum = 0
	for i in range(0, len(lines), 10):
		rows = lines[i + 1: i + 10]
		board = []
		for row in rows:
			board.append([int(row[i]) for i in range(len(row.strip()))])
		is_solved = solve(board)
		if not is_solved:
			is_solved, board = guess_and_solve(board)
		triple = board[0][0:3]
		sum += int(''.join([str(i) for i in triple]))
	print(sum)
		

	