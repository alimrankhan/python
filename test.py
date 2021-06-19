#lcs #dp #long_common_subsequence

def lcs(str1,str2):
	m=len(str1)
	n=len(str2)
	ans=[]
	l=0
	for i in range(0,m):
		for j in range(0,n):
			
			if str1[i]==str2[j]:
				l=l+1
				ans.append(str1[i])
			
			
	return ans,l
a='abcde'
b='bace'
print(lcs(a,b))
