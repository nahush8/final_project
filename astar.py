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
sigma = 1
#print numOfVertices
#print startingVertex
#print goalVertex
goalCoordinateX,goalCoordinateY = coordList[goalVertex-1]
goalCoordinateX = float(goalCoordinateX)
goalCoordinateY = float(goalCoordinateY)

def heuristics(vertices):

	x,y = coordList[vertices-1]
	x = float(x)
	y = float(y)
	return sigma * sqrt((x-goalCoordinateX)*(x-goalCoordinateX)+(y-goalCoordinateY)*(y-goalCoordinateY))

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
parent = [-999] * (numOfVertices+1)
parent[startingVertex] = -1
#print openList
#print closedList
#print cost

while True:	
	for vertices in openList:
		tempCostList.append((vertices, cost[vertices]) +  heuristics(vertices)))
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
print cost[goalVertex]
print len(closedList)
printPath(parent,goalVertex)
