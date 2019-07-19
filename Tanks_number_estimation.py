from math import factorial as fac
from random import randint as rd

def f(k):
	p=0
	mx=max(k)
	m=len(k)
	i=mx
	while (p<0.99):
		p+=fac(i-m)*(m-1)*fac(mx-1)/(fac(i)*fac(mx-m))
		i+=1
	return (mx,i-1,p);

N=1000
m=50
h=[x+1 for x in range(N)]
k=[]
for x in range(m):
	r=rd(0,len(h)-1)
	k.append(h[r])
	del h[r]
print(k)
print(f(k))








