import sys

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
		tempCostList.append((vertices,cost[vertices]))
	print tempCostList
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
	
	
	print "open"
	print openList
	print "close"
	print closedList

print cost[goalVertex]
print len(closedList)
