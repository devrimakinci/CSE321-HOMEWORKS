# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

"""Basamak sayısına göre karşılaştırma yaptım. Eğer basamak sayısı 3 den küçük olursa -1 dönecek. Basamak sayısı
hem 3 un hem de 5 in katı ise sayı basamak sayısı kadar 5 olucak. Örnek:15 basamak sayısı Sayı ->555555555555555
Eğer basamak sayısı 3 ün katıysa basamak sayısı kadar sayı da 5 olucak. Basamak sayısı 5 ile bölümünden kalan 0,1,2,3 veya 4 ise
ve 3 ile bölümünde kalan 2 ise o zaman sayı ,5 tane 3 sayısı, basamak sayısının 5 eksiği kadar 5 sayısını içerecektir.
Basamak sayısı 5 ile bölümünden kalan 0,1,2,3 veya 4 ise ve 3 ile bölümünde kalan 1 ise o zaman sayı ,10 tane 3 sayısı, 
basamak sayısının 10 eksiği kadar 5 sayısını içerecektir. Basamak sayısı 5 in katı ve basamak sayısını 15'ten küçükse o zaman
sayı basamak sayısı kadar 3 içerecektir. Aksi durumda ise fonksiyon -1 döner. Bu karşılaştırmaları PDF'de verilen özelliklere göre yaptım."""

def decentNumber(digit):
	result = []
	string  = ""
	if (digit < 3):
		return -1
	elif (digit % 5 == 0 and digit % 3 == 0):
		for i in range(digit):
			result.append(5)
	elif (digit % 3 == 0):
		for i in range(digit):
			result.append(5)
	elif (abs(digit - 5) % 3 == 0 and digit < 15):
		numberThree = digit - 5
		numberFive = digit - numberThree
		for i in range(numberThree):
			result.append(5)
		for i in range(numberFive):
			result.append(3)
	elif (abs(digit - 3) % 5 == 0 and digit < 15):
		numberFive = digit - 3
		numberThree = digit - numberFive
		for i in range(numberThree):
			result.append(5)
		for i in range(numberFive):
			result.append(3)
	elif (digit % 5 == 0 and digit < 15):
		for i in range(digit):
			result.append(3)
	elif(digit - 5 > 5 and ((digit % 5 == 0 or digit % 5 == 1 or digit % 5 == 2 or digit % 5 == 3 or digit % 5 == 4) and digit % 3 == 2)):
		numberFive = 5
		numberThree = digit - numberFive
		for i in range(numberThree):
			result.append(5)
		for i in range(numberFive):
			result.append(3)
	elif(digit - 5 > 5 and ((digit % 5 == 0 or digit % 5 == 1 or digit % 5 == 2 or digit % 5 == 3 or digit % 5 == 4) and digit % 3 == 1)):
		numberFive = 10
		numberThree = digit - numberFive
		for i in range(numberThree):
			result.append(5)
		for i in range(numberFive):
			result.append(3)
	else:
		return -1
	for data in result:
		string += str(data)
	return string

dn = decentNumber(11)
print(dn)