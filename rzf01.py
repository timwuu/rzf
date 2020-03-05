# https://mathworld.wolfram.com/RiemannZetaFunction.html
# https://mathworld.wolfram.com/RiemannZetaFunctionZeros.html
#
# http://www.dtc.umn.edu/~odlyzko/zeta_tables/index.html

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

    while i < n:
        if i%p==0:
            if i%q==0:
                xi += (q-p)*i**(-s)
            else:
                xi -= p*i**(-s)
        else:
            if i%q==0:
                xi += q*i**(-s)

        i += 1

    return xi

n = 100001

sigma = 0.5

t = 14.13472514 # first
t = 21.022040   # second
t = 25.010858   # third
t = 30.424876
t = 32.935062
t = 37.586178

#t = 23.0

s = complex( sigma, t)

#zeta = calcZeta(s, 2, n) 
#print( zeta)

#zeta = calcZeta(s, 5, n) 
#print( zeta)

#zeta = calcZeta(s, 7, n) 
#print( zeta)

t = 13.1

while t < 50.1:
    s = complex( sigma, t)
    zetaDiff = calcZetaDiff( s, 13, 23, n)
    if abs(zetaDiff) < 0.05:
        print( "{0:.2f}    {1:.5f}".format( t, zetaDiff))
    t += 0.01