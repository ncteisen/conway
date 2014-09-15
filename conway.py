import os
import time

class Cell:

	def __init__(self):
		self.neighbors = 0
		self.value = ' '

class Board:

	def __init__(self, size=10):
		self.board = [[Cell() for _ in range(size)] for _ in range(size)]
		self.size = size
		self.age = 0

	def set_cell(self, row, col):
		assert row < self.size
		assert col < self.size
		self.board[row][col].value = '#'
		self.update_board()

	def clear_cell(self, row, col):
		assert row < self.size
		assert col < self.size
		self.board[row][col].value = ' '
		self.update_board()

	def count_neighbors(self, row, col):
		count = 0
		if row - 1 >= 0 and col - 1 >= 0 and self.board[row - 1][col - 1].value == '#' : count += 1
		if row - 1 >= 0 and self.board[row - 1][col].value == '#' : count += 1
		if row - 1 >= 0 and col + 1 < self.size and self.board[row - 1][col + 1].value == '#' : count += 1
		if row + 1 < self.size and col - 1 >= 0 and self.board[row + 1][col - 1].value == '#' : count += 1
		if row + 1 < self.size and self.board[row + 1][col].value == '#' : count += 1
		if row + 1 < self.size and col + 1 < self.size and self.board[row + 1][col + 1].value == '#' : count += 1
		if col - 1 >= 0 and self.board[row][col - 1].value == '#' : count += 1
		if col + 1 < self.size and self.board[row][col + 1].value == '#' : count += 1
		return count

	def update_board(self):

		# count up the neighbors for each cell
		for i,row in enumerate(self.board):
			for j,cell in enumerate(row):
				cell.neighbors = self.count_neighbors(i, j)


	def tick(self):

		self.age += 1

		# decide the fate of the cell
		for row in self.board:
			for cell in row:
				if cell.value == '#':
					# lonely cell
					if cell.neighbors < 2 : cell.value = ' '
					# overcrowded cell
					elif cell.neighbors > 3 : cell.value = ' '
					# stable cell
					else : pass
				else:
					# birth of a cell
					if cell.neighbors == 3 : cell.value = '#'

		self.update_board()

	def print_board(self):
		os.system('clear')
		print '--' * self.size + '---'
		for row in self.board:
			print '|',
			for cell in row:
				print cell.value,
			print '|'
		print '--' * self.size + '---'
		print "Generation %d" % self.age

	def run(self):
		resp = ' '
		while resp != 'q' and resp != 'Q' and resp != 'quit':
			self.print_board()
			self.tick()
			resp = raw_input()

	def run_auto(self, wait):
		while True:
			self.print_board()
			self.tick()
			time.sleep(wait)

if __name__ == "__main__":
	b = Board(45)

	"""
	# glider
	b.set_cell(10,10)
	b.set_cell(10,11)
	b.set_cell(10,12)
	b.set_cell(9,12)
	b.set_cell(8,11)
	"""
	
	# r-pentamino
	b.set_cell(25,25)
	b.set_cell(24,25)
	b.set_cell(26,25)
	b.set_cell(25,24)
	b.set_cell(24,26)
	

	"""
	b.set_cell(25,25)
	b.set_cell(24,25)
	b.set_cell(26,25)
	b.set_cell(26,27)
	b.set_cell(26,26)
	b.set_cell(27,27)
	b.set_cell(24,24)
	b.set_cell(24,23)
	b.set_cell(28,27)
	"""
	"""
	# 10 line loop
	b.set_cell(20,20)
	b.set_cell(20,21)
	b.set_cell(20,22)
	b.set_cell(20,23)
	b.set_cell(20,24)
	b.set_cell(20,25)
	b.set_cell(20,26)
	b.set_cell(20,27)
	b.set_cell(20,28)
	b.set_cell(20,29)
	"""
	"""
	# beacon
	b.set_cell(20,20)
	b.set_cell(20,21)
	b.set_cell(21,21)
	b.set_cell(21,20)
	b.set_cell(22,22)
	b.set_cell(22,23)
	b.set_cell(23,22)
	b.set_cell(23,23)
	"""
	b.run()






