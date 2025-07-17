def gcd(x, y):
	r = x % y
	
	if r == 0:
		return y
	elif y == 0:
		return x
		
	return gcd(y, r)

def lcm(x, y):
	return x*y // gcd(x, y)

def solve():
	x, y = map(int, input().split())
	print(gcd(x, y))
	print(lcm(x, y))
	
solve()