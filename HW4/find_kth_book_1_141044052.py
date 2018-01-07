# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

""" Her iki arrayin ortadaki indeksini arraylarin size'ina göre buluyoruz. İki arrayin
ortadaki indekslerinin toplamı k'dan küçükse  m[mid1] > n[mid2] ise demek ki aradığımız değer
n'nin diğer elemanlarından büyük olduğu için n arrayini küçültüyoruz. Aksi durumda aradığımız değer m'nin
diğer elemanlarından büyük olduğu için m arrayini küçültürüz. Bu işlemi recursive olarak base case takılana 
kadar sürdürürüz ve aradığımız kth elemanı bulmuş oluruz. 
Bu algoritmanın time complexity ise arrayin sizelarına göre ortadaki indeksi bulduğumuz için
O(logm + logn)'dir."""

def find_kth_book_1(m,n,k):
	temp1 = []
	temp2 = []
	string = helperFindKthBook1(m,n,temp1,temp2,k)
	return string

def helperFindKthBook1(m,n,temp1,temp2,k):
	if (len(m) == len(temp1)):
		return (n[k - 1])
	if (len(n) == len(temp2)):
		return (m[k - 1])
	mid1 = (len(m) - len(temp1)) // 2
	mid2 = (len(n) - len(temp2)) // 2
	if (mid1 + mid2 < k - 1):
		if (m[mid1] > n[mid2]):
			n = n[mid2 + 1:]
			return helperFindKthBook1(m,n,temp1,temp2,k - mid2 - 1)
		else:
			m = m[mid1 + 1:]
			return helperFindKthBook1(m,n,temp1,temp2,k - mid1 - 1)
	else:
		if(m[mid1] > n[mid2]):
			temp1 = m[mid1:]
			return helperFindKthBook1(m,n,temp1,temp2,k)
		else:
			temp2 = n[mid2:]
			return helperFindKthBook1(m,n,temp1,temp2,k)


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_1(m,n,5)
print(book)
