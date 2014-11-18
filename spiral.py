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
				

