import sys
from math import sqrt

coordList = []
coordFile = 'coords_3.txt'
with open(coordFile) as f2:
	data = f2.readlines()
f2.close()
data = [x.strip() for x in data] #Getting the input data from the file
for z in range(0,len(data)):
	coordList.append((data[z].split()[0],data[z].split()[1]))


fname = sys.argv[1]
with open(fname) as f:
	data = f.readlines()
f.close()
data = [x.strip() for x in data] #Getting the input data from the file
numOfVertices = int(data[0])
startingVertex = int(data[1])
goalVertex = int(data[2])
print numOfVertices
print startingVertex
print goalVertex
goalCoordinateX,goalCoordinateY = coordList[goalVertex-1]
goalCoordinateX = float(goalCoordinateX)
goalCoordinateY = float(goalCoordinateY)


MAN_WEIGHT = 0
EUC_WEIGHT = 0
EUC_SQUARE_WEIGHT = 0
DIAG_WEIGHT = 0

if MAN_WEIGHT + EUC_WEIGHT + EUC_SQUARE_WEIGHT + DIAG_WEIGHT != 1:
	exit()

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

openList = []
closedList = []
cost = [float("inf")] * (numOfVertices+1)
cost[startingVertex] = 0
openList.append(startingVertex)
tempCostList = []
#print openList
#print closedList
#print cost

while True:	
	for vertices in openList:
		tempCostList.append((vertices, cost[vertices] + 
							(MAN_WEIGHT * man_heuristics(vertices) + EUC_WEIGHT * euc_heuristics(vertices))+ 
							(DIAG_WEIGHT * diag_heuristics(vertices) + EUC_SQUARE_WEIGHT * euc_square_heuristics(vertices))))
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
					if i not in openList:
						openList.append(i)
	
	
	#print "open"
	#print openList
	#print "close"
	#print closedList
print "COST OF THE GOAL"
print cost[goalVertex]
print "NUMBER OF ITERATIONS"
print len(closedList)


