'''
Given an integer, , perform the following conditional actions:

		If n is odd, print Weird
		If n is even and in the inclusive range of  to , print Not Weird
		If n is even and in the inclusive range of  to , print Weird
		If n is even and greater than , print Not Weird
'''

n=int(input("enter the number :"))
if n % 2 !=0:
    print("weird")
elif n>=2 and n<=5:
    print("not weird")
elif n>=6 and n<=20:
    print("weird")
else:
    print("not weird")