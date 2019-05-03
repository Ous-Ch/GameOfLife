# Conway : Game Of Lif By Ousssama-Ch

from Tkinter import *
from random import randrange

def grid():
    i, j = 4, 4 
    while i < ay :
        can.create_line(0, i, ax, i, width=1, fill='darkgray')
        i += 4
    while j < ax :
        can.create_line(j, 0, j, ay, width=1, fill='darkgray')
        j += 4        

def draw():
	can.delete(ALL)
	grid()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			x = j*4+2
			y = i*4+2
			if matrix[i][j] == 1:
				can.create_rectangle(x-1, y-1, x+2, y+2, width=0, fill='black')
	
	root.after(20, nextEtat)

def count_neighbour(i,j):
	nb = 0
	if matrix[(i-1+cy)%cy][(j-1+cx)%cx] == 1:
		nb += 1
	if matrix[(i+cy)%cy][(j-1+cx)%cx] == 1:
		nb += 1
	if matrix[(i+1+cy)%cy][(j-1+cx)%cx] == 1:
		nb += 1
	if matrix[(i-1+cy)%cy][(j+cx)%cx] == 1:
		nb += 1
	if matrix[(i+1+cy)%cy][(j+cx)%cx] == 1:
		nb += 1
	if matrix[(i-1+cy)%cy][(j+1+cx)%cx] == 1:
		nb += 1
	if matrix[(i+cy)%cy][(j+1+cx)%cx] == 1:
		nb += 1
	if matrix[(i+1+cy)%cy][(j+1+cx)%cx] == 1:
		nb += 1
	return nb

def nextEtat():
	todie, tocreate = [], []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			n = count_neighbour(i,j)
			if (n < 2 or n > 3) and matrix[i][j] == 1:
				todie.append((i,j))
			if n == 3 and matrix[i][j] == 0:
				tocreate.append((i,j))

	for d in todie:
		matrix[d[0]][d[1]] = 0
	for c in tocreate:
		matrix[c[0]][c[1]] = 1

	draw()

def random():
	k = 0
	while k < 2000:
		i = randrange(0, cy)
		j = randrange(0, cx)
		matrix[i][j] = 1
		k += 1

# main #
root = Tk()
root.title("Game Of Life - By Oussama-Ch")

ax, ay = 400, 300
cx, cy = ax/4, ay/4

matrix = [[0 for j in range(cx)] for i in range(cy)]
random()
#matrix[0][-1] = 1
#matrix[0][0] = 1
#matrix[0][1] = 1

can = Canvas(root, width=ax, height=ay, bg='white')
can.grid(row=0, column=0)

draw()

root.mainloop()
