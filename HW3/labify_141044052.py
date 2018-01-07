# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

class myQueue():

	def __init__(self):
		self.data = []

	def isEmpty(self):
		if (len(self.data) == 0):
			return True
		else:
			return False

	def peek(self):
		if (self.isEmpty() == True):
			return None
		else:
			return self.data[0]

	def size(self):
		return (len(self.data))

	def offer(self,element):
		last = self.size()
		self.data.insert(last,element)

	def poll(self):
		if (self.isEmpty() == True):
			return None
		else:
			returnValue = self.data.pop(0)
			return returnValue

def listSearch(searchList,element):
	found = -1
	for i in range(len(searchList)):
		if (searchList[i] == element):
			found = i
			return found
	return found			


def breadthFirstSearch(graph,start):
	visitList = []
	road = 0
	queue = myQueue()
	queue.offer(start)
	visitList.append(start)
	while (queue.isEmpty() == False):
		vertex = queue.poll()
		neighbourList = list (graph[vertex])
		for i in range(len(neighbourList)):
			neighbour = neighbourList[i]
			if (listSearch(visitList,neighbour) == -1):
				queue.offer(neighbour)
				visitList.append(neighbour)
				road = road + 1

	return visitList,road

def findDisconnectedVertex(graph):
	disconnected = set()
	disconnectedList = []
	for i in graph:
		temp,noneUsed = breadthFirstSearch(graph,i)
		temp.sort()
		temp = tuple(temp)
		disconnected.add(temp)

	myList = list(disconnected)
	for i in range(len(myList)):
		disconnectedList.append(myList[i][0])

	disconnectedList.sort()
	return disconnectedList

def findMinimumCostToLabifyGTU(buildCost,roadCost,graph):
	cost = 0
	road = 0
	costList = []
	size = len(graph)
	if (size == 1):
		cost = buildCost
		return cost
	elif (buildCost <= roadCost):
		size = len(graph)
		cost = cost + (size * buildCost)
		return cost
	else:		
		disconnectedList = findDisconnectedVertex(graph)
		for i in range(len(disconnectedList)):
			visitList, road = breadthFirstSearch(graph,disconnectedList[i])
			costList.append(road)
		for i in range(len(costList)):
			cost = cost + (costList[i] * roadCost)
		cost = cost + (len(disconnectedList) * buildCost)
		return cost

def testCode():

	mapOfGTU = {
		1 : set([2,3]),
		2 : set([1,4]),
		3 : set([1,4]),
		4 : set([2,3]),
		5 : set([5,7]),
		6 : set([5,7]),
		7 : set([5,6]),
		8 : set([])
	}

	minCost = findMinimumCostToLabifyGTU(5,2,mapOfGTU)

	print ("Minimum Cost:",minCost)

testCode()	
