# Adi: Devrim
# Soyadi: AKINCI
# Numarasi: 141044052

rottenWalnutList=[2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] # Test etmek icin tanimlanan liste

global globalSize # Yukaridaki listenin size'ini tutan global bir degisken

globalSize = len(rottenWalnutList)

# compareScales
# Bu fonksiyon iki listenin elemanlarini toplar ve onlari birbirinden cikarir.
# Sonuc negatif ise 1, pozitif ise -1, esit ise 0 dondurur.
# Parametreleri
# leftScaleList - Birinci Liste
# rightScaleList - Ikinci Liste

def compareScales (leftScaleList, rightScaleList):
	result = sum(leftScaleList) - sum(rightScaleList)
	if result < 0:
		return 1
	elif result > 0:
		return -1
	else:
		return 0

# inList
# Bu fonksiyon verilen listenin elemanlarinin ayni olup olmadigina bakar.
# Ayni ise True, farkli ise False dondurur.
# Parametreleri
# List - Liste

def inList(List):
	size = len(List)
	i = 0
	dif = False
	while i != size-1:
		if List[i] != List[i+1]:
			dif = True
			return dif
		else:
			dif = False
		i = i+1
	return dif

# findRottenWalnut
# Bu fonksiyon recursive bir sekilde verilen listedeki farkli olan sayinin listedeki yerini dondurur.
# Parametreleri
# walnutList - Liste

def findRottenWalnut(walnutList):
	if len(walnutList) == 1:
		return 0
	size = len(walnutList)
	if size % 2 == 1:
		size = size + 1 
	half = size // 2
	halfList = walnutList[0:half] # Listenin yariya bolunmesi
	restOfList = walnutList[half:size]
	result = compareScales(halfList,restOfList)
	if result == 1: # Listenin sol tarafinin alinmasi
		res = len(walnutList)//2 + findRottenWalnut(halfList)
	elif result == -1:
		if len(walnutList) % 2 == 1: # Eger listenin eleman sayisi tek sayi ise
			if inList(halfList) == True: # Farkli sayi listenin solunda ise listenin solunun alinmasi
				res = len(halfList) + findRottenWalnut(halfList)-1
			else: # Aksi halde listenin sag tarafinin alinmasi
				res = len(walnutList) + findRottenWalnut(restOfList)+1
		else: # Listenin sag tarafinin alinmasi
			res = len(walnutList) + findRottenWalnut(restOfList)			
	else: # Eger listede farkli bir eleman yok ise
		return -1

	# Listedeki farkli sayinin listedeki indexinin bulunmasi
	if globalSize == len(walnutList): 
		return res - len(walnutList) + 1

	return res

print (findRottenWalnut(rottenWalnutList)) # findRottenWalnut fonksiyonun cagrilmasi