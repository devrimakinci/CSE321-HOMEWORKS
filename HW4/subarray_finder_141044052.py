# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

"""Divide and conquer ile verilen arrayi bir elemanlı olana kadar parçaladım ve
tek elemalı bütün arrayleri karşılaştırarak minimum olanı bulup bir üst level'a taşıdım.
Bu işlemi recursion bitene kadar devam ettirdim ve minimum subarrayi buldum ve return ettim."""

def findMinVal (arr1,arr2): # İki arrayi karşılaştırır ve minimum olanı return eder.
	sum1 = 0
	sum2 = 0
	for data1 in arr1:
		sum1 += data1
	for data2 in arr2:
		sum2 += data2
	if(sum1 > sum2):
		return arr2
	else:
		return arr1

def min_subarray_finder(arr):
	if (len(arr) == 1):
		return arr
	temp = arr[1:]
	myList1 = min_subarray_finder(temp)
	temp2 = arr[0:len(arr) - 1]
	myList2 = min_subarray_finder(temp2)
	val1 = findMinVal(temp,temp2)
	val2 = findMinVal(myList1,myList2)
	return findMinVal(val1,val2)

inpArr = [1, -4, -7, 5, -13, 9, 23, -1]

msa = min_subarray_finder(inpArr)
print(msa)
print(sum(msa))