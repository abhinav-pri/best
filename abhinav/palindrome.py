def palindrome():
 str=input("enter your string")
 flag=0;
 if(str==str[::-1]):
	 print("yes")
 else:
	 print("No")			
	 
if __name__== "__main__":
	palindrome()
