# https://mathworld.wolfram.com/RiemannZetaFunction.html
# https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html

import cmath

def calcZeta( s, p, n):

    i=1
    xi = 0.0

    p_1=p-1

    while i < n:
        if i%p==0:
            xi -= p_1*i**(-s)
        else:
            xi += i**(-s)
        
        i += 1

    zeta = xi/( 1.0 - p**(1.0-s))

    return zeta

def calcZetaDiff( s, p, q, n):

    i=1
    xi = 0.0

    p_1=p-1
    q_1=q-1

    while i < n:
        if i%p==0:
            if i%q==0:
                xi += (q_1-p_1)*i**(-s)
            else:
                xi -= p*i**(-s)
        else:
            if i%q==0:
                xi += q*i**(-s)

        i += 1

    return xi

n = 10000001

sigma = 0.5

t = 14.13472514 # first
t = 21.022040   # second
t = 25.010858   # third
t = 30.424876
t = 32.935062
t = 37.586178

#t = 23.0

s = complex( sigma, t)

i=1

#zeta = calcZeta(s, 2, n) 
#print( zeta)

#zeta = calcZeta(s, 5, n) 
#print( zeta)

#zeta = calcZeta(s, 7, n) 
#print( zeta)

zetaDiff = calcZetaDiff( s, 23, 37, n)
print( zetaDiff)