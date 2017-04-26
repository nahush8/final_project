import sys
from math import sqrt
import numpy as np
coordList = []
coordFile = 'coords_3.txt'
with open(coordFile) as f2:
	data = f2.readlines()
f2.close()
data = [x.strip() for x in data] #Getting the input data from the file
for z in range(0,len(data)):
	coordList.append((data[z].split()[0],data[z].split()[1]))

def printPath(parent,j):
	if parent[j] == -1:
		return
	printPath(parent,parent[j])
	print j

fname = sys.argv[1]
with open(fname) as f:
	data = f.readlines()
f.close()
data = [x.strip() for x in data] #Getting the input data from the file
numOfVertices = int(data[0])
startingVertex = int(data[1])
goalVertex = int(data[2])
#print numOfVertices
#print startingVertex
#print goalVertex
goalCoordinateX,goalCoordinateY = coordList[goalVertex-1]
goalCoordinateX = float(goalCoordinateX)
goalCoordinateY = float(goalCoordinateY)


MAN_WEIGHT = 1
EUC_WEIGHT = 1
EUC_SQUARE_WEIGHT = 1
DIAG_WEIGHT = 1

def euc_heuristics(vertices):

	x,y = coordList[vertices-1]
	x = float(x)
	y = float(y)
	return sqrt((x-goalCoordinateX)*(x-goalCoordinateX)+(y-goalCoordinateY)*(y-goalCoordinateY))

def man_heuristics(vertices):

	x,y = coordList[vertices-1]
	x = float(x)
	y = float(y)
	return abs(x-goalCoordinateX) + abs(y-goalCoordinateY)

def euc_square_heuristics(vertices):

	x,y = coordList[vertices-1]
	x = float(x)
	y = float(y)
	return (x-goalCoordinateX)*(x-goalCoordinateX)+(y-goalCoordinateY)*(y-goalCoordinateY)

def diag_heuristics(vertices):

	x,y = coordList[vertices-1]
	x = float(x)
	y = float(y)
	dx = abs(x-goalCoordinateX)
	dy = abs(y-goalCoordinateY)
	return max(dx,dy)


graph = []
adj = [[-99 for i in xrange(numOfVertices+1)] for i in xrange(numOfVertices+1)]
for x in range(3,len(data)):
	a = int(data[x].split()[0])
	b = int(data[x].split()[1])
	c = float(data[x].split()[2])
	graph.append([a,b,c]) #Creating a graph of vertices and edges
	adj[a][b] = c #creating an adjacency matrix


#print openList
#print closedList
#print cost
parent = [-999] * (numOfVertices+1)
parent[startingVertex] = -1
f = open('data.txt','w')
'''
for i1 in range(1,10):
	for i2 in range(1,10):
		for i3 in range(1,10):
			for i4 in range(1,10):	
'''
'''
MAN_WEIGHT = float(i1) / float(i1 + i2 + i3 + i4)
EUC_WEIGHT = float(i2) / float(i1 + i2 + i3 + i4)
DIAG_WEIGHT = float(i3) / float(i1 + i2 + i3 + i4)
EUC_SQUARE_WEIGHT = float(i4) / float(i1 + i2 + i3 + i4)

MAN_WEIGHT = round(MAN_WEIGHT,2)
EUC_WEIGHT = round(EUC_WEIGHT,2)
DIAG_WEIGHT = round(DIAG_WEIGHT,2)
EUC_SQUARE_WEIGHT = round(EUC_SQUARE_WEIGHT,2)
'''
MAN_WEIGHT = 0
EUC_WEIGHT = 0
DIAG_WEIGHT = 0
EUC_SQUARE_WEIGHT = 0


l1 = np.arange(0,1,0.01)
for i1 in l1:
	MAN_WEIGHT = i1
	EUC_WEIGHT = 1 - MAN_WEIGHT

	openList = []
	closedList = []
	cost = [float("inf")] * (numOfVertices+1)
	cost[startingVertex] = 0
	openList.append(startingVertex)
	tempCostList = []
	while True:	
		for vertices in openList:
			tempCostList.append((vertices, cost[vertices] + 
								(MAN_WEIGHT * man_heuristics(vertices) + EUC_WEIGHT * euc_heuristics(vertices))))#+ 
								#(DIAG_WEIGHT * diag_heuristics(vertices) + EUC_SQUARE_WEIGHT * euc_square_heuristics(vertices))))
		#print tempCostList
		minCostVertex,minCost = min(tempCostList, key = lambda t: t[1])
		tempCostList[:] = []
		
		del openList[openList.index(minCostVertex)]
		closedList.append(minCostVertex)
		
		if minCostVertex == goalVertex:
			break
		
		for i in range(1,numOfVertices+1):
				if adj[minCostVertex][i] != -99:
					if i not in closedList:
						costNew = cost[minCostVertex] + adj[minCostVertex][i]
						if cost[i] > costNew:
							cost[i] = costNew
							parent[i] = minCostVertex
						if i not in openList:
							openList.append(i)					
		#print "open"
		#print openList
		#print "close"
		#print closedList
	#output = str(MAN_WEIGHT) + "\t" + str(EUC_WEIGHT) + "\t" + str(EUC_SQUARE_WEIGHT) + "\t" + str(DIAG_WEIGHT) + "\t\t" + str(len(closedList)) + "\n"
	output = str(MAN_WEIGHT) + "\t" + str(EUC_WEIGHT) + "\t\t" + str(len(closedList)) + "\t\t" + str(cost[goalVertex]) + "\n"
	print output
	f.write(output)
	f.flush()
print "NUMBER OF ITERATIONS"
#print len(closedList)
#print cost[goalVertex]
f.close()
printPath(parent,goalVertex)