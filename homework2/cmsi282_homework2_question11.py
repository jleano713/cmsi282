# algorithm for modular exponentiation credit: 
# http://aditya.vaidya.info/blog/2014/06/27/modular-exponentiation-python/
def expmod(a, b, c):
	x = 1
	while(b > 0):
		if (b & 1 == 1):
			x = (x * a) % c
		a = (a * a) % c
		b >>= 1
	return x % c

def stacked_expmod(a, b, c, p):
	d = expmod(b, c, p - 1)
	return expmod(a, d, p)


print(str(expmod(2,125,127)))