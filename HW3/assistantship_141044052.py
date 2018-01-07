# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

import sys


def swapTwoValues (myList,i,j):
	temp = myList[i]
	myList[i] = myList[j]
	myList[j] = temp
	return myList


def permutation (permList):
	temp = []
	returnList = []
	for i in range(len(permList)):
		temp.append(0)		
	returnList.append(tuple(permList))
	i = 0
	size = len(permList)
	while i < size:
		if (temp[i] < i):
			if (i % 2 == 0):
				permList = swapTwoValues(permList,0,i)
			else:
				permList = swapTwoValues(permList,temp[i],i)

			returnList.append(tuple(permList))
			temp[i] = temp[i] + 1
			i = 0
		else:
			temp[i] = 0
			i = i + 1

	return returnList

def findOptimalAssistantship(table):
	courseSize = len(table[0])
	raSize = len(table)
	costList = []
	returnList = []
	minimum = 0
	if (courseSize > raSize):
		print ("Error: Number of course is larger than number of research assistant!")
		sys.exit()
	elif (courseSize == 1 and raSize == 1):
		returnList.append(0)
		minimum = table[0][0]
		return returnList,minimum
	elif (courseSize == raSize):
		myList = list(range(courseSize))
		permList = permutation(myList)
		for i in range(len(permList)):
			cost = 0
			assistantIndex = 0
			for j in range(len(permList[i])):
				courseIndex = permList[i][j]
				cost = cost + table[assistantIndex][courseIndex]
				assistantIndex = assistantIndex + 1
			costList.append(cost)
		minimum = (min(costList))
		indexMin = costList.index(minimum)
		returnList = list(permList[indexMin])
	else:
		myList = list(range(raSize))
		permList = permutation(myList)
		for i in range(len(permList)):
			cost = 0
			assistantIndex = 0
			permList[i] = list(permList[i])
			for j in range(len(permList[i])):
				if (courseSize <= permList[i][j]):
					permList[i][j] = -1
			for j in range(len(permList[i])):
				courseIndex = permList[i][j]
				if (courseIndex == -1):
					cost = cost + 6
				else:
					cost = cost + table[assistantIndex][courseIndex]
				assistantIndex = assistantIndex + 1
			costList.append(cost)
		minimum = (min(costList))
		indexMin = costList.index(minimum)
		returnList = list(permList[indexMin])

	return returnList,minimum


def testCode():

	inputTable = [[5,8,7],[8,12,7],[4,8,5]]
	asst, time = findOptimalAssistantship(inputTable)
	print (asst)
	print (time)

testCode()
