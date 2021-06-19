#lcs #dp #long_common_subsequence

def lcs(str1,str2):
	m=len(str1)
	n=len(str2)
	ans=[]
	l=0
	for i in range(0,m+1):
		for j in range(0,n+1):
			if i==0 or j==0:
				t[i][j]=0 **
			
			elif str1[i]==str2[j]:
				t[i][j]= 1+t[i-1][j-1]
				ans.append(str1[i])
			
			else:
				t[i][j]= max(t[i][j-1],t[i-1][j])
	
	return t[m][n],ans
lcs('imran','khan')

