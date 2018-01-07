# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

""" Verilen Y arrayinden belirlenen formüle göre X arrayini çıkarttım. X arrayini çıkarırken X arrayinin elemanlarını formüle göre
maksimum olmasını sağladım.
Worst Case Analysis
W(n) = O(n) dir. """

def findNumberOne(arr):
	found = False
	for data in arr:
		if(data == 1):
			found = True
	return found

def findXArr(arr):
	flag = findNumberOne(arr)
	if (flag):
		if(arr[0] == 1 and arr[1] == 1):
			for i in range(len(arr)):
				if(i % 2 == 1):
					arr[i] = 1
			return arr
		else:
			tmp = []
			result1 = 0
			result2 = 0
			for i in range(1,len(arr)-1):
				if (arr[i] != 1):
				 	if(arr[i-1] == 1):
				 		arr[i+1] = 1
				 	elif(arr[i+1] == 1):
				 		arr[i-1] = 1
			for i in range(1,len(arr)):
				result1 += abs(arr[i] - arr[i-1])
			index = arr.index(1)
			if(index % 2 == 0):
				for i in range(len(arr)):
					if(i % 2 == 0):
						tmp.append(1)
					else:
						tmp.append(arr[i])
			else:
				for i in range(len(arr)):
					if(i % 2 != 0):
						tmp.append(1)
					else:
						tmp.append(arr[i])
			for i in range(1,len(tmp)):
				result2 += abs(tmp[i] - tmp[i-1])
			if (result1 > result2):
				return arr
			else:
				return tmp
	else:
		tmp = []
		sum1 = 0
		sum2 = 0
		for i in range(len(arr)):
			if(i % 2 == 1):
				tmp.append(arr[i])
				arr[i] = 1
			elif(i % 2 == 0):
				tmp.append(1)
		sum1 = sum(arr)
		sum2 = sum(tmp)
		if(sum1 > sum2):
			return arr
		else:
			return tmp

def find_maximum_cost(arr):
	result = 0
	newArr = findXArr(arr)
	for i in range(1,len(newArr)):
		result += abs(newArr[i] - newArr[i-1])
	return result

def test():
	Y1 = [14,1,14,1,14]
	cost1 = find_maximum_cost(Y1)
	print("cost1",cost1)
	#Output: 52
	Y2 = [1,9,11,7,3]
	cost2 = find_maximum_cost(Y2)
	print("cost2",cost2)
	#Output: 28
	Y3 = [50,28,1,1,13,7]
	cost3 = find_maximum_cost(Y3)
	print("cost3",cost3)
	#Output: 78

test()