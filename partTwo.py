import math  

def main():
#TO DO  
 A = int(input("What is A?"))
 B = int(input("What is B?"))
 pythag(A,B)

def pythag(A,B):
#TO DO  
 n = ((A**2)+ (B**2))
 print(n)
 c = int(math.sqrt(n))
 print(c)
main()
