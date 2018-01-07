# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

""" İlk olarak birinci satır birinci sütuna baktım. 2.sütuna geçebileceği cell'in max değerini buldum ve 2.sütuna geçtim. Bu işlemi
sütun sayısı kadar yaptım ve gezdiğim cell'leri bir listeye attım. Daha sonra ikinci satır için aynı şeyi yaptım. Bu işlemi ise satır
sayısı kadar yaptım. Elimde artık her satır için max değeri veren yolların listesi var. Bunların içerisinden max olanı buldum ve return
ettim. 
Worst Case Analysis
W(n) = O(n*m) dir. """

def theft(money):
	i = 0
	j = 0
	index = 0
	result = 0
	stealList = []
	tempList = []
	myList = []
	possibleList = []
	sumList = []
	rowSize = len(money)
	colSize = len(money[i])
	for k in range(rowSize):
		myList.append(money[k][j])
	for i in range(len(myList)):
		j += 1
		possibleList.append(myList[i])
		while (j < colSize):
			right = i
			rightUp = i - 1
			rightDown = i + 1
			if (rightUp < 0):
				tempList.append(money[right][j])
				tempList.append(money[rightDown][j])
				maxMoney = max(tempList)
				possibleList.append(maxMoney)
				index = tempList.index(maxMoney)
				if(index == 0):
					i = right
				elif (index == 1):
					i = rightDown
			elif (rightDown >= rowSize):
				tempList.append(money[right][j])
				tempList.append(money[rightUp][j])
				maxMoney = max(tempList)
				possibleList.append(maxMoney)
				index = tempList.index(maxMoney)
				if(index == 0):
					i = right
				elif (index == 1):
					i = rightUp
			else:
				tempList.append(money[right][j])
				tempList.append(money[rightDown][j])
				tempList.append(money[rightUp][j])
				maxMoney = max(tempList)
				possibleList.append(maxMoney)
				index = tempList.index(maxMoney)
				if(index == 0):
					i = right
				elif (index == 1):
					i = rightDown
				elif (index == 2):
					i = rightUp
			j += 1
			tempList = []
		stealList.append(possibleList)
		possibleList = []
		j = 0
	if (len(stealList) == 1):
		result = sum(stealList[0])
		return result
	else:
		for data in stealList:
			sumList.append(sum(data))
		result = max(sumList)
		return result

def test():
	amountOfMoneyInLand = [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
	amountOfMoneyInLand2 = [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
	res1 = theft(amountOfMoneyInLand)
	res2 = theft(amountOfMoneyInLand2)
	print(res1)
	print(res2)

test()