# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

""" Bir önceki soruda ortadaki indeksi arrayin size'ina göre bulmak yerine burada ortadaki indeksi
k'ya göre buluyoruz. Eğer m'nin ve n'nin size'i half'fan büyükse i ve j'ye half değerini atıyoruz. Aksi
durumda i'ye m'nin size'ini j'ye de n'nin size'ini atıyoruz. m[i-1] > n[j-1] ise demek ki aradığımız değer
n'nin diğer elemanlarından büyük olduğu için n arrayini küçültüyoruz. Aksi durumda aradığımız değer m'nin
diğer elemanlarından büyük olduğu için m arrayini küçültürüz. Bu işlemi recursive olarak base case takılana 
kadar sürdürürüz ve aradığımız kth elemanı bulmuş oluruz.
Bu algoritmanın time complexity ise arrayin ortadaki indeksini k'ya göre bulduğumuz için
O(logk)'dır."""

def find_kth_book_2(m,n,k):
	if(len(m) > len(n)): # Eger m nin size n den buyukse
		return find_kth_book_2(n,m,k)
	if(len(m) == 0):
		return (n[k - 1])
	if(k == 1):
		if(m[0] > n[0]):
			return n[0]
		else:
			return m[0]
	half = k // 2
	if (len(m) > half):
		i = half
	else:
		i = len(m)
	if (len(n) > half):
		j = half
	else:
		j = len(n)
	if(m[i - 1] > n[j - 1]):
		n = n[j:]
		return find_kth_book_2(m,n,k-j)
	else:
		m = m[i:]
		return find_kth_book_2(m,n,k-i)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_2(m,n,5)
print(book)