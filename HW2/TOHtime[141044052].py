# Adi: Devrim
# Soyadi: AKINCI
# Numarasi: 141044052

elapsedlist=[] # Disklerin baska yere tasinma surelerini tutan bir liste
diskList = ["SRC","AUX","DST"] # Disklerin tasinacak yerlerin adlarini tutan liste

# towersOfHanoi
# Bu fonksiyon disklerin nereden nereye hareket ettigini gosteren bir stringi konsola basar.
# Ayrica disklerin tasinma surelerini bulup onları elapsedList'e ekler.

def towersOfHanoi(source,auxiliary,destination,diskWeighted):
	if diskWeighted == 1:
		index = diskList.index(destination) - diskList.index(source) # Pegs araliginin bulunmasi
		if index < 0:
			index = index * -1
		if len(elapsedlist) == 0: # Eger elapsedList bos ise o listeye birinci diskin tasinma suresini ekler.
			print ("disk ",diskWeighted,": ",source, "to" ,destination)
			elapsedlist.append(diskWeighted * index)
		else: # Eger elapsedList bos degilse birinci diskin tasinma suresini listenin basina ekler.
			print ("disk ",diskWeighted,": ",source, "to" ,destination)
			elapsedlist[diskWeighted-1] = elapsedlist[diskWeighted-1] + diskWeighted * index
	else:
		towersOfHanoi(source,destination,auxiliary,diskWeighted-1) 
		print ("disk ",diskWeighted,": ",source, "to" ,destination) 
		index = diskList.index(destination) - diskList.index(source) # Pegs araliginin bulunmasi
		if index < 0:
			index = index * -1
		if len(elapsedlist) == diskWeighted-1:
			elapsedlist.append(diskWeighted * index) # Recursive olarak diskin tasinma surelerinin listeye eklenmesi
		else:
			elapsedlist[diskWeighted-1] = elapsedlist[diskWeighted-1] + diskWeighted * index # Listenin update edilmesi
		towersOfHanoi(auxiliary,source,destination,diskWeighted-1)

# printElapsedTime
# Bu fonksiyon disklerin tasinma surelerini konsola basar		

def printElapsedTime(timeList):
	for i in range(len(timeList)):
		print("Elapsed time for disk ",i+1,": ",timeList[i])
		

towersOfHanoi(diskList[0],diskList[1],diskList[2],3) # towersOfHanoi fonksiyonun cagrilmasi
printElapsedTime(elapsedlist) # printElapsedTime fonksiyonun cagrilmasi