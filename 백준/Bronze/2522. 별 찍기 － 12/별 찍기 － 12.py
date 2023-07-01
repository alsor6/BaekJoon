a = int(input())
for i in range(1,a+1):
    print(" "*(a-i),"*"*i, sep="")
for i in range(1,a):
    print(" "*i, "*"*(a-i), sep="")