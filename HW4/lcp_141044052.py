# Adi : Devrim
# Soyadi : AKINCI
# Numarasi : 141044052

""" Arrayi ilk olarak ortadaki elemana göre ikiye böleriz. Böldükten sonra arrayin sol tarafındaki
ve sağ tarafındaki 2 stringi alarak o stringlerin common postfixini buluruz ve return ederiz. Diger level'da
buldugumuz common postfix olan stringlerin common postfixini bularak recursion'a devam ederiz.
Worst Case
Eğer arrayin içerisindeki stringler aynı ise o zaman worst case meydana gelir.
Örnek olarak stringin uzunluğu n olsun. İki stringin common postfixini bulurken
stringin tüm elemanlarına bakmak gerekecek. Bunun time complexity'si O(n)'dir. Arrayin
size ise m olsun. W(NM)'dir."""


def longest_common_postfix(arr):
	lcp = helperLCP(arr,0,len(arr)-1)
	return lcp

def helperLCP(arr,first,last):
	if (first == last):
		return arr[first]
	if (last > first):
		mid = first + ((last - first) // 2)
		string1 = helperLCP(arr,first,mid)
		string2 = helperLCP(arr,mid+1,last)
		return findCommonPostfixTwoString(string1,string2)

def findCommonPostfixTwoString(string1,string2):
	res = ""
	i = len(string1) - 1
	j = len(string2) - 1
	while ((i >= 0 and j >= 0) and (string1[i] == string2[j])):
		res = string1[i] + res
		i = i - 1
		j = j - 1
	return res

inpStrings = ["absorptivity","circularity","electricity","importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)