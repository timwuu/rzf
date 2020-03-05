import cmath


n = 300001

sigma = 0.5

t = 14.13472514 # first
t = 21.022040   # second
t = 25.010858   # third

#t = 22

s = complex( sigma, t)

i=1

eta = 0.0

while i < n:
    if i%2==1:
        eta += i**(-s)
    else:
        eta -= i**(-s)
    
    i += 1

#print(eta)

zeta = eta/( 1.0 - 2.0**(1.0-s))

print( zeta)
#print( eta)


i=1

xi = 0.0

p=3
p_1=p-1

while i < n:
    if i%p==0:
        xi -= p_1*i**(-s)
    else:
        xi += i**(-s)
    
    i += 1

zeta = xi/( 1.0 - p**(1.0-s))

#print(xi)
print( zeta)


