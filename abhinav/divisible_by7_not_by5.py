def divi(l,r):

	for  x in range(l,r+1):
		if x%7==0 and x%5!=0:
			print(x)
		
if __name__ == "__main__":
	l=int(input("enter the left index = "))
	r=int(input("enter the right index = "))
	divi(l,r)
	
