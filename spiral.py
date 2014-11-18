#!/usr/bin/python

def spiral(rows, cols):
	row, col, count, uLim, lLim = 0, 0, 0, 0, 0
	dLim = cols
	rLim = rows
	maxCube = dLim * rLim
	dir = 'right'

	while (count <= maxCube):
		if dir == 'right':
			if col < rLim:
				count += 1
				col += 1
				#array - something like [dLim][rLim]
			else: 
				dir = 'down'
				uLim += 1;

		if dir == 'down':
			if row < dLim:
				count += 1
				row += 1
				#array
			else:
				dir = 'left'
				rLim -= 1

		if dir == 'left':
			if col >= lLim:
				counter += 1
				col -= 1
				#array
			else:
				dir = 'up'
				dLim += 1

		if dir == 'up':
			if row >= uLim:
				count += 1
				row -= 1
				#array
			else:
				dir = 'right'
				lLim += 1
				col -= 1

	print #thearray - which will be [dLim][rLim];


