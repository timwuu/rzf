import math

def calcXi( s, p, n):

    i=1
    xi = 0.0

    p_1=p-1

    while i < n:
        if i%p==0:
            xi -= p_1*i**(-s)
        else:
            xi += i**(-s)
        
        i += 1

    return xi

n=100001

p = 11

print( calcXi( 1.0, p, n))

print( math.log(p))