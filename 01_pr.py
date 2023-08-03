a = int( input ("Enter your number "))
b = int( input ("Enter your number "))
c = int( input ("Enter your number "))

def diff (b,n,m):
    if b>n and b>m:
        return b
    elif n>b and n>m:
        return n
    elif m>b and m>n:
        return m
    else:
        return "Error"

print( "Greatest number is " ,diff(a,b,c))
