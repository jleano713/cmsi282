def lcm(x, y):
	return (x * y) / gcd(x, y)

def gcd(x, y):
	if (x == 0):
		return y
	return gcd((y % x), x)