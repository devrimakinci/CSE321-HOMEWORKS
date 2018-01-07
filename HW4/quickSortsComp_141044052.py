# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141004052

"""Hoare partition pivotu arrayin ilk elemanı olarak seçer. Lomuto partition ise pivotu arrayin son elemanı
olarak seçer.Hoare partition time complexity O(n)'dir. Lomuto partition time complexity ise O(n)'dir."""

# QUICKSORT LOMUTO PARTITION
def quickSortLomuto(arr):
	helperQuickSortLomuto(arr,0,len(arr)-1)

def helperQuickSortLomuto(arr,low,high):
	if (low < high):
		pivot = lomutoPartition(arr,low,high)
		helperQuickSortLomuto(arr,low,pivot - 1)
		helperQuickSortLomuto(arr,pivot + 1,high)

def lomutoPartition(arr,low,high):
	pivot = arr[high]
	i = low - 1
	j = low
	while (j <= high - 1):
		if (arr[j] <= pivot):
			i = i + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		j = j + 1
	temp = arr[i+1]
	arr[i+1] = arr[high]
	arr[high] = temp
	return i + 1

# QUICKSORT HOARE PARTITION
def quickSortHoare(arr):
	helperQuickSortHoare(arr,0,len(arr)-1)

def helperQuickSortHoare(arr,low,high):
	if (low < high):
		pivot = hoarePartition(arr,low,high)
		helperQuickSortHoare(arr,low,pivot)
		helperQuickSortHoare(arr,pivot+1,high)

def hoarePartition(arr,low,high):
	pivot = arr[low]
	i = low
	j = high
	while True:
		while (arr[i] < pivot):
			i = i + 1
		while (arr[j] > pivot):
			j = j - 1			
		if (i >= j):
			return j
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp

# TEST
arr = [15,4,68,24,75,16,42]
quickSortLomuto(arr)
print("Lombo",arr)
quickSortHoare(arr)
print("Hoare",arr)